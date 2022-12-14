from django.utils.datetime_safe import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse

from cooking_co.cocktails.models import Cocktail
from cooking_co.tests.common.base_test_case import BaseTestCase

UserModel = get_user_model()

def create_non_alcoholic_cocktails_for_user(user, count=4):
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
def create_alcoholic_cocktails_for_user(user, count=4):
    result = []
    for i in range(count):
        cocktail = Cocktail(
            cocktail_name=f"Ice Cola {i + 1}",
            main_ingredient='whiskey',
            other_ingredient='175ml coca-cola, 25ml ice{i+1}',
            cocktail_photo=f'https://www.cc.com/images/icecola{i + 1}.jpg',
            user=user,
        )
        cocktail.save()
        result.append(cocktail)

class ProfileIndexViewTests(BaseTestCase):
    VALID_USER_DATA = {
        'email': 'bogoivanov@abv.bg',
        'password': 'Cooking1234.',
        'date_of_birth': datetime.strptime("2000-11-11", "%Y-%m-%d"),
    }
    def test_anonymous_user_cant_see_alcoholic_cocktails(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(0, response.context['alcoholic_cocktails'])

    def test_anonymous_user_age_of_user_16(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(0, response.context['alcoholic_cocktails'])
        self.assertEqual(16, response.context['age_of_user'])

    def test__profile_age_less_than_21_cant_see_alcoholic_cocktails(self):
        user = self.create_and_login_user(**self.VALID_USER_DATA)

        create_non_alcoholic_cocktails_for_user(user, count=4)
        create_alcoholic_cocktails_for_user(user, count=4)
        response = self.client.get(reverse('index'))
        self.assertEqual(4, response.context['non_alcoholic_cocktails'])
        self.assertEqual(4, response.context['alcoholic_cocktails'])
        self.assertEqual(4, response.context['all_articles_without_alcohol'])
    def test_anonymous_user_age_cant_see_alcoholic_cocktails(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        self.client.login(**self.VALID_USER_DATA)
        create_non_alcoholic_cocktails_for_user(user, count=4)
        create_alcoholic_cocktails_for_user(user, count=4)
        self.client.logout()
        response = self.client.get(reverse('index'))
        self.assertEqual(4, response.context['non_alcoholic_cocktails'])
        self.assertEqual(4, response.context['alcoholic_cocktails'])
        self.assertEqual(4, response.context['all_articles_without_alcohol'])


