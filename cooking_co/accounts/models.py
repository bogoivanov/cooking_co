from django.contrib.auth.models import AbstractUser
from cooking_co.accounts.helpers.get_age import get_age_profile
from cooking_co.accounts.managers import UserManager
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models
from cooking_co.accounts.validators.validate_age_over_16 import at_least_16
from cooking_co.accounts.validators.validate_birthdate_not_in_past import birthday_not_in_future
from cooking_co.accounts.validators.validate_image_size import validate_file_less_than_5mb
from cooking_co.accounts.validators.validate_only_letters import validate_only_letters


class AppUser(AbstractUser):
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
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to='profile-pictures/',
        null=True,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )

    gender = models.CharField(
        choices=GENDERS,
        max_length=15,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        validators=(birthday_not_in_future, at_least_16,),
    )

    age = models.IntegerField(
        null=True,
        blank=True,
    )
    ready_for_moderator = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )
    ready_for_moderator_email = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.age = get_age_profile(self.date_of_birth)
        return super().save(*args, **kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', ]
    objects = UserManager()
    ordering = ('email',)
