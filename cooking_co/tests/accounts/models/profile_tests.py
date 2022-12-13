from unittest import TestCase

from django.contrib.auth import get_user_model

UserModel = get_user_model()
class ProfileModelTests(TestCase):
    def test_profile_save__when_date_of_birth_correct__expect_correct_result(self):
        profile = UserModel(
            email='bogoivanov@abv.bg',
            password1='Cooking1234.',
            password2='Cooking1234.',
            date_of_birth='2000-11-11',
        )

        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile.pk)