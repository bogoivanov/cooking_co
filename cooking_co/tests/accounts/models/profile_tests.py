from django.core.exceptions import ValidationError
from django.test import TestCase

from django.contrib.auth import get_user_model

from cooking_co.accounts.models import AppUser
UserModel=get_user_model()

class ProfileModelTests(TestCase):
    def test_profile_save__when_date_of_birth_correct__expect_correct_result(self):
        profile = UserModel(
            email='bogoivanov@abv.bg',
            password='Cooking1234.',
            date_of_birth='2000-11-11',
        )
        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_date_of_birth_correct_set_age__expect_correct_result(self):
        profile = UserModel(
            email='bogoivanov@abv.bg',
            password='Cooking1234.',
            date_of_birth='2000-11-11',
        )
        profile.full_clean()
        profile.save()

        self.assertEqual(22, profile.age)

    def test_profile_save__when_date_of_birth_correct_set_age_under_21__expect_correct_result(self):
        profile = UserModel(
            email='bogoivanov@abv.bg',
            password='Cooking1234.',
            date_of_birth='2004-11-11',
        )
        profile.full_clean()
        profile.save()

        self.assertEqual(18, profile.age)
    def test_profile_save__when_date_of_birth_in_future__expect_exception(self):
        profile = UserModel(
            email='bogoivanov@abv.bg',
            password='Cooking1234.',
            date_of_birth='2030-11-11',
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save__when_date_of_birth_less_than_16__expect_exception(self):
        profile = UserModel(
            email='bogoivanov@abv.bg',
            password='Cooking1234.',
            date_of_birth='2020-11-11',
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)
    def test_profile_save__when_first_name_has_digit__expect_exception(self):
        profile = UserModel(
            email='bogoivanov@abv.bg',
            password='Cooking1234.',
            date_of_birth='2000-11-11',
            first_name='Bogo1',
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save__when_first_name_one_letter__expect_exception(self):
        profile = UserModel(
            email='bogoivanov@abv.bg',
            password='Cooking1234.',
            date_of_birth='2000-11-11',
            first_name='B',
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

