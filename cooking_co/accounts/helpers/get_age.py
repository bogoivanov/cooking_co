from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date
from django.core import exceptions


def get_age_profile(birthdate):

    today = date.today()
    one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
    year_difference = today.year - birthdate.year
    age = year_difference - one_or_zero
    return age
