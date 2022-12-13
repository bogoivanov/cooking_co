from django.contrib.auth import get_user_model
from django.core import validators
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify


UserModel = get_user_model()


# Create your models here.



class Cocktail(models.Model):
    MIN_NAME = 2
    MAX_NAME = 30
    NON_ALCOHOLIC = 'non-alcoholic'
    VODKA = 'vodka'
    WHISKEY = 'whiskey'
    LIQUORS = 'liquors'
    RUM = 'rum'
    GIN = 'gin'
    TEQUILA = 'tequila'
    INGREDIENTS = [(x, x) for x in (NON_ALCOHOLIC, VODKA, WHISKEY, LIQUORS, RUM, GIN, TEQUILA)]

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
        default='non-alcoholic',
        null=False,
        blank=True,
    )

    other_ingredient = models.CharField(
        max_length=150,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.cocktail_name} with {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(f'{self.cocktail_name}-{self.id}')
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['cocktail_name']
