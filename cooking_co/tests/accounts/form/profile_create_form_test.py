from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy

from cooking_co import settings
from cooking_co.cocktails.models import Cocktail
from cooking_co.common.models import CocktailLike
from cooking_co.tests.common.base_test_case import BaseTestCase

UserModel = get_user_model()


def create_cocktails_for_user(user, count=4):
    result = []
    for i in range(count):
        cocktail = Cocktail(
            cocktail_name=f"Ice Cola {i + 1}",
            main_ingredient='non-alcoholic',
            other_ingredient='175ml coca-cola, 25ml ice{i+1}',
            cocktail_photo=f'https://www.cc.com/images/icecola{i + 1}.jpg',
            user=user,
        )
        cocktail.save()
        result.append(cocktail)


class ProfileEditViewTests(BaseTestCase):
    VALID_USER_DATA = {
        'email': 'bogoivanov@abv.bg',
        'password': 'Cooking1234.',
        'date_of_birth': datetime.strptime("2000-11-11", "%Y-%m-%d"),
    }

    def test__profile_edit_and_add_data_correct(self):
        profile_data = {
            'first_name': 'Bogo',
            'last_name': 'Ivanov',
            'gender': 'Male',
        }

        user = self.create_and_login_user(**self.VALID_USER_DATA)
        response = self.client.post(reverse_lazy('user edit', kwargs={'pk': user.pk}), data=profile_data)
        created_profile = UserModel.objects.filter(**profile_data).get()

        self.assertIsNotNone(created_profile)
        self.assertEqual(302, response.status_code)

    def test__profile_edit_anonymous_user__expect_to_redirect_to_login(self):
        profile_data = {
            'first_name': 'Bogo',
            'last_name': 'Ivanov',
        }

        response = self.client.post(reverse_lazy('user edit', kwargs={'pk': 1}), data=profile_data)

        self.assertEqual(302, response.status_code)
        self.assertEqual(settings.LOGIN_URL + f'?next=/accounts/profile/edit/1/', response.headers.get('Location'))


def create_likes_for_user_and_cocktails(user, cocktails):
    current = 0
    total_likes_count = 0
    for cocktail in cocktails:
        for i in range(current):
            CocktailLike(
                cocktail=cocktail,
                user=user,
            ).save()
            total_likes_count += 1
        current += 1
        current = int(current)
    return total_likes_count


class ProfileDetailsViewTests(BaseTestCase):
    VALID_USER_DATA = {
        'email': 'bogoivanov@abv.bg',
        'password': 'Cooking1234.',
        'date_of_birth': datetime.strptime("2000-11-11", "%Y-%m-%d"),
    }

    def test__profile_details_when_owner(self):
        user = self.create_and_login_user(**self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('user details', kwargs={'pk': user.pk}))
        self.assertTrue(response.context['is_owner'])

    def test__profile_details_when_not_owner_expect_false(self):
        not_owner_user_data = {
            'email': 'bogoivanov@abv.bg1',
            'password': 'Cooking1234.',
            'date_of_birth': datetime.strptime("2000-11-11", "%Y-%m-%d"),
        }

        not_owner_user = self.create_and_login_user(**not_owner_user_data)

        user = self.create_and_login_user(**self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('user details', kwargs={'pk': not_owner_user.pk}))
        self.assertFalse(response.context['is_owner'])

    def test__profile_details_when_no_cocktails_expect_empty(self):
        user = self.create_and_login_user(**self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('user details', kwargs={'pk': user.pk}))
        self.assertCollectionEmpty(response.context['cocktails'])
        self.assertEqual(0, response.context['cocktails_count'])

    def test__profile_details_when_no_recipes_expect_empty(self):
        user = self.create_and_login_user(**self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('user details', kwargs={'pk': user.pk}))
        self.assertCollectionEmpty(response.context['recipes'])
        self.assertEqual(0, response.context['recipes_count'])

    def test__profile_details_when_cocktails_and_no_likes_expect_empty(self):
        user = self.create_and_login_user(**self.VALID_USER_DATA)
        create_cocktails_for_user(user, count=4)
        response = self.client.get(reverse_lazy('user details', kwargs={'pk': user.pk}))
        self.assertEqual(4, len(response.context['cocktails']))
        self.assertEqual(4, response.context['cocktails_count'])

    def test__profile_details_when_cocktails_and_likes_expect_to_see_likes_count(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        self.client.login(**self.VALID_USER_DATA)
        create_cocktails_for_user(user, count=4)
        response = self.client.get(reverse_lazy('user details', kwargs={'pk': user.pk}))
        cocktails = response.context['cocktails']
        not_owner_user_data = {
            'email': 'bogoivanov@abv.bg1',
            'password': 'Cooking1234.',
            'date_of_birth': datetime.strptime("2000-11-11", "%Y-%m-%d"),
        }
        not_owner_user = UserModel.objects.create_user(**not_owner_user_data)
        cocktail_likes = create_likes_for_user_and_cocktails(not_owner_user, cocktails)
        self.client.logout()
        self.client.login(**self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('user details', kwargs={'pk': user.pk}))
        self.assertEqual(cocktail_likes, response.context['total_likes_count'])

