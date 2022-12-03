from django.db import models

# Create your models here.
# auth_app/models.py
from django.contrib.auth import models as auth_models
from django.db import models
from django.urls import reverse

from cooking_co.accounts.managers import UserManager
from django.utils.translation import gettext_lazy as _
from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models


# from petstagram.core.model_mixins import ChoicesEnumMixin
# from petstagram.core.validators import validate_only_letters


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    FEMALE = 'Female'
    MALE = 'Male'
    GENDERS = [(x, x) for x in (MALE, FEMALE)]

    username = None

    email = models.EmailField(_('email address'), unique=True)

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),

        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),

        )
    )
    profile_image = models.URLField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        choices=GENDERS,
        max_length=15,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(

    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', ]
    objects = UserManager()
    ordering = ('email',)
# class AppUserww(auth_models.User):
#     pass
# ~Extening AbstractBaseUser~
# class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
#     first_name = models.CharField(
#         max_length=15,
#         null=False,
#         blank=False,
#     )
#
#     last_name = models.CharField(
#         max_length=15,
#         null=False,
#         blank=False,
#     )
#
#     email = models.EmailField(
#         unique=True,
#         null=False,
#         blank=False,
#     )
#
#     date_joined = models.DateTimeField(
#         auto_now_add=True,
#         null=False,
#         blank=False,
#     )
#
#     is_staff = models.BooleanField(
#         default=False,
#         null=False,
#         blank=False,
#     )
#     date_of_birth = models.DateField(
#         null=True,
#         blank=True,
#     )
#
#     # User credentials consist of `email` and `password`
#     USERNAME_FIELD = 'email'
#
#     objects = AppUserManager()
#
#
# class Profile(models.Model):
#     first_name = models.CharField(
#         max_length=15,
#         null=True,
#         blank=True,
#     )
#
#     last_name = models.CharField(
#         max_length=15,
#         null=True,
#         blank=True,
#     )
#
#     profile_image = models.URLField(
#         null=True,
#         blank=True,
#     )
#
#     birth_date = models.DateTimeField(
#         null=True,
#         blank=True,
#     )
#
#     user_key = models.OneToOneField(
#         AppUser,
#         primary_key=True,
#         on_delete=models.CASCADE,
#     )
#
#     def get_absolute_url(self):
#         return reverse('profile details', kwargs={'pk': self.pk})
#     # @property
#     # def age(self, value):
#     #     names = value.split(' ')
#     #     self.first_name = names[0]
#     #     self.last_name = names[1]
