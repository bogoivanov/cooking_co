from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


# Create your models here.


class Recipe(models.Model):
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

    ON_TASTE = 'on taste'
    ON_EYE = 'on eye'
    SALT = [(x, x) for x in (ON_TASTE, ON_EYE)]

    recipe_name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
        validators=(validators.MinLengthValidator(MIN_NAME),)
    )

    recipe_photo = CloudinaryField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=False,
        blank=True,
    )

    main_ingredient = models.CharField(
        choices=INGREDIENTS,
        max_length=30,
        null=False,
        blank=False,
    )

    other_ingredient = models.CharField(
        max_length=150,
    )

    prepare = models.TextField(
        max_length=400,
        null=False,
        blank=False,
    )
    salt = models.CharField(
        choices=SALT,
        max_length=10,
        null=False,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.recipe_name} with id: {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(f'{self.recipe_name}-{self.id}')
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['recipe_name']
