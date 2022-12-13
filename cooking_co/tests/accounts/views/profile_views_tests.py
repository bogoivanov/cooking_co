from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils.datetime_safe import date, datetime
from django.contrib.auth import get_user_model
from django.urls import reverse

from cooking_co.cocktails.models import Cocktail
from cooking_co.tests.common.base_test_case import BaseTestCase

UserModel = get_user_model()


class ProfileIndexViewTests(BaseTestCase):

    def test_anonymous_user_cant_see_alcoholic_cocktails(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(0, response.context['alcoholic_cocktails'])

    def test_anonymous_user_age_of_user_16(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(16, response.context['age_of_user'])
        self.assertEqual(0, response.context['alcoholic_cocktails'])

    def test__profile_age_less_than_21_cant_see_alcoholic_cocktails(self):
        # TODO
        cocktails_count = 2
        cocktail_alcoholic = Cocktail.objects.create(
            pk=1,
            cocktail_name="Margaritha",
            main_ingredient='tequila',
            other_ingredient='75ml tequila, 25ml triple sec, 100ml orange liquer, salt',
            cocktail_photo='https://www.cc.com/images/margarita1.jpg',
        )
        cocktail_non_alcoholic = Cocktail(
            pk=2,
            cocktail_name="Ice Cola",
            main_ingredient='non-alcoholic',
            other_ingredient='175ml coca-cola, 25ml ice',
            cocktail_photo='https://www.cc.com/images/icecola1.jpg',
        )

        credentials = {
            'email': 'bogoivanov@abv.bg',
            'password': 'Cooking1234.',
            'date_of_birth': datetime.strptime("2000-11-11", "%Y-%m-%d"),
        }

        self.create_and_login_user(**credentials)

        all_cocktails = cocktail_alcoholic | cocktail_non_alcoholic
        print(all_cocktails)
        UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)
        response = self.client.get(reverse('index'))
        self.assertEqual(cocktails_count, len(all_cocktails))
        self.assertEqual(len(all_cocktails), response.context['all_cocktails'])

