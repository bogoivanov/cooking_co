from django.core import exceptions
from django.utils.datetime_safe import date


def birthday_not_in_future(birthdate):
    if birthdate > date.today():
        raise exceptions.ValidationError("The date cannot be in the future!")


