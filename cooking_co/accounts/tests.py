from unittest import TestCase

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse

from cooking_co.accounts.forms import UserCreateForm
from cooking_co.common.tests import BaseTestCase
from django.core.exceptions import ValidationError
from django.test import TestCase

UserModel = get_user_model()

class AppUserModelTests(TestCase):
    # Triple A - Arrange, Act, Assert

    def test_profile_save__with_correct_values__expect_success(self):
        # Arrange
        profile = UserModel(

            email='bogoivanov@abv.com',
            password='Cooking1234.',
            first_name= 'Bogo',
            last_name= 'Ivanov',
            date_of_birth='2000-11-11'
        )

        # Act
        profile.full_clean()  # Call this for validation
        profile.save()

        # Assert
        self.assertIsNotNone(profile.pk)

    def test_profile_save__with_incorrect_name__expect_exception(self):
        # Arrange
        profile = UserModel(
            email='bogoivanov@abv.com',
            password='Cooking1234.',
            first_name='Bogo',
            last_name='Ivanov',
            date_of_birth='2020-11-11'
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save__with_incorrect_name__expect_exception(self):
        # Arrange
        profile = UserModel(
            email='bogoivanov@abv.com',
            password='Cooking1234.',
            first_name='Bogo',
            last_name='Ivanov',
            date_of_birth='2020-11-11'
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)
# # TODO
# # from testing_demos.web.models import Profile
# # from tests.common.base_test_case import BaseTestCase
#
# class ProfileCreateFormTests(TestCase):
#     def test_profile_create_form_disabled_fields__when_all__expect_all_to_be_disabled(self):
#         form = UserCreateForm()
#         disabled_fields = {
#             name: field.widget.attrs[UserCreateForm.disabled_attr_name]
#             for name, field in form.fields.items()
#         }
#
#         self.assertEqual(
#             UserCreateForm.disabled_attr_name,
#             disabled_fields['name'],
#         )
#         self.assertEqual(
#             UserCreateForm.disabled_attr_name,
#             disabled_fields['age'],
#         )
#         self.assertEqual(
#             UserCreateForm.disabled_attr_name,
#             disabled_fields['egn'],
#         )
#
#     def test_profile_create_form_disabled_fields__when_name_is_disabled__expect_name_to_be_disabled(self):
#         # monkey patching
#         UserCreateForm.disabled_fields = ('name',)
#         form = UserCreateForm()
#         disabled_fields = {
#             name: field.widget.attrs[UserCreateForm.disabled_attr_name]
#             for name, field in form.fields.items()
#             if UserCreateForm.disabled_attr_name in field.widget.attrs
#         }
#
#         self.assertEqual(
#             UserCreateForm.disabled_attr_name,
#             disabled_fields['name'],
#         )
#         self.assertEqual(1, len(disabled_fields))
#
# class ProfileCreateViewTests(BaseTestCase):
#     def test_create_profile__when_user_is_loggedin__expect_to_create_profile(self):
#         profile_data = {
#             'name': 'Doncho',
#             'age': 19,
#             'egn': 1234567890,
#         }
#         credentials = {
#             'username': 'doncho',
#             'password': 'doncho123',
#         }
#
#         self.create_and_login_user(**credentials)
#
#         response = self.client.post(
#             reverse('create profile'),
#             data=profile_data,
#         )
#
#         created_profile = UserModel.objects.filter(**profile_data) \
#             .get()
#
#         self.assertIsNotNone(created_profile)
#         self.assertEqual(302, response.status_code)
#
#     def test_create_profile__when_anonymous_user__expect_to_redirect_to_login(self):
#         profile_data = {
#             'name': 'Doncho',
#             'age': 19,
#             'egn': 1234567890,
#         }
#
#         response = self.client.post(
#             reverse('create profile'),
#             data=profile_data,
#         )
#         self.assertEqual(302, response.status_code)
#         expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("create profile")}'
#         self.assertEqual(expected_redirect_url, response.headers.get('Location'))
# from django.contrib.auth import get_user_model
# from django.urls import reverse
#
#
#
#
# class ProfileListViewTests(BaseTestCase):
#     def test_profiles_list_view__when_no_profiles__expect_empty_list_and_count_context(self):
#         # Act
#         # `self.client.get()` makes HTTP GET request
#         response = self.client.get(reverse('list profiles'))
#
#         # Assert
#         self.assertCollectionEmpty(response.context['profile_list'])
#         self.assertEqual(0, response.context['profiles_count'])
#
#     def test_profiles_list_view__when_profiles__expect_list_of_profiles_and_header_count(self):
#         # Arrange
#         profiles_count = 9
#         profiles = [
#             UserModel.objects.create(
#                 name=f'Test User {i}',
#                 age=20 + i,
#                 egn=f'123456789{i}'
#             )
#             for i in range(1, profiles_count + 1)
#         ]
#
#         # Act
#         response = self.client.get(reverse('list profiles'))
#
#         # Assert
#         self.assertListEqual(profiles, list(response.context['profile_list']))
#         self.assertEqual(profiles_count, response.context['profiles_count'])
#
#     def test_profiles_list_view__when_anonymous_user__username_to_be_anonymous(self):
#         # Act
#         response = self.client.get(reverse('list profiles'))
#
#         # Assert
#         self.assertEqual('Anonymous', response.context['username'])
#
#     def test_profiles_list_view__when_loggedin_user__username_to_be_correct(self):
#         # Arrange
#         username = 'doncho'
#         # User creation can be moved to an `utils` module
#         credentials = {
#             'username': username,
#             'password': username,
#         }
#
#         self.create_and_login_user(**credentials)
#
#         # Act
#         response = self.client.get(reverse('list profiles'))
#
#         # Assert
#         self.assertEqual(username, response.context['username'])
#
#     # def test_profiles_list_view__when_query_is_provided__expect_query_to_be_in_context(self):
#     #     # Act
#     #     response = self.client.get(
#     #         reverse('list profiles'),
#     #         data={
#     #             'query': 'the-query',
#     #         })
#     #
#     #     # Assert
#     #     self.assertEqual('the-query', response.context['query'])
#
#
#
#
#
#
# class ProfileModelTests(TestCase):
#     # 3A - Arrange, Act, Assert
#     #      Setup,   Do,  Check result
#
#     def test_profile_save__when_egn_is_valid__expect_correct_result(self):
#         # Arrange
#         profile = UserModel(
#             name='Doncho',
#             age=19,
#             egn='0310230467',
#         )
#
#         # Act
#         profile.full_clean()  # Call this for validation
#         profile.save()
#
#         # Assert
#         self.assertIsNotNone(profile.pk)
#
#     def test_profile_save__when_egn_is_has_9_digits__expect_exception(self):
#         # Arrange
#         profile = UserModel(
#             name='Blagoy',
#             date_of_birth='2000-11-11',
#         )
#
#         with self.assertRaises(ValidationError) as context:
#             profile.full_clean()
#             profile.save()
#
#         self.assertIsNotNone(context.exception)
#
#
#
#
#
#
#
#
#
#
#
