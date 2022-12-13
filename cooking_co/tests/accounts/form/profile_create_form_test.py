import tempfile
from datetime import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy

from cooking_co import settings
from cooking_co.accounts.models import AppUser
from cooking_co.tests.common.base_test_case import BaseTestCase

UserModel = get_user_model()


class ProfileEditViewTests(BaseTestCase):

    def test__profile_edit_and_add_data_correct(self):
        profile_data = {
            'first_name': 'Bogo',
            'last_name': 'Ivanov',
            'gender': 'Male',
            # 'profile_image': tempfile.NamedTemporaryFile(suffix=".jpg"),
        }

        credentials = {
            'email': 'bogoivanov@abv.bg',
            'password': 'Cooking1234.',
            'date_of_birth': datetime.strptime("2000-11-11", "%Y-%m-%d"),
        }

        user = self.create_and_login_user(**credentials)
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
        self.assertEqual(settings.LOGIN_URL+f'?next=/accounts/profile/edit/1/', response.headers.get('Location'))
