from django.contrib.auth import get_user_model
from django.core import validators
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from cooking_co.accounts.helpers.get_age import get_age_profile

AppUser = get_user_model()


# Create your models here.
class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f'{name}={value}' for (name, value) in fields)


class Cocktail(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'cocktail_name')
    MIN_NAME = 2
    MAX_NAME = 30
    NON_ALCOHOLIC = 'non-alcoholic'
    VODKA = 'vodka'
    WHISKEY = 'whiskey'
    LIQUEURS = 'liquers'
    RUM = 'rum'
    GIN = 'gin'
    TEQUILA = 'tequila'
    INGREDIENTS = [(x, x) for x in (NON_ALCOHOLIC, VODKA, WHISKEY, LIQUEURS, RUM, GIN, TEQUILA)]

    cocktail_name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
        validators=(validators.MinLengthValidator(MIN_NAME),)
    )

    cocktail_photo = models.URLField(
        null=False,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    main_ingredient = models.CharField(
        choices=INGREDIENTS,
        max_length=30,
    )

    other_ingredient = models.CharField(
        max_length=30,
    )

    user = models.ForeignKey(
        AppUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.cocktail_name} with {self.id}"

    def save(self, *args, **kwargs):
        # Create/Update
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.cocktail_name}-{self.id}')
        # Update
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['cocktail_name']
