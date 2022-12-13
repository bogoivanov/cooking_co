from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.utils.text import slugify


UserModel = get_user_model()


# Create your models here.
class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f'{name}={value}' for (name, value) in fields)


class Recipe(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'cocktail_name')
    MIN_NAME = 2
    MAX_NAME = 30

    PORK = 'pork'
    CHICKEN = 'chicken'
    BEEF = 'beef'
    FISH = 'fish'
    SEAFOOD = "seafood"
    EGGS = 'eggs'
    VEGETARIAN = 'vegetarian'
    VEGAN = 'vegan'
    INGREDIENTS = [(x, x) for x in (PORK, CHICKEN, BEEF, FISH, SEAFOOD, EGGS, VEGETARIAN, VEGAN)]

    recipe_name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
        validators=(validators.MinLengthValidator(MIN_NAME),)
    )

    recipe_photo = models.URLField(
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
        return f"{self.recipe_name} with {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.recipe_name}-{self.id}')
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['recipe_name']
