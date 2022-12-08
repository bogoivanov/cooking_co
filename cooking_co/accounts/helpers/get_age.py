from django.utils.datetime_safe import date


def get_age_profile(birthdate):
    today = date.today()
    one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
    year_difference = today.year - birthdate.year
    age = year_difference - one_or_zero
    return age

