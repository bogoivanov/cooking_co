from django.core import exceptions
from django.utils.datetime_safe import date


def at_least_16(birthdate):
    today = date.today()
    one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
    year_difference = today.year - birthdate.year
    difference = year_difference - one_or_zero - 16
    print(f"{difference} dif")
    if difference < 0:
        raise exceptions.ValidationError("You must to be at least 16 years old!")


