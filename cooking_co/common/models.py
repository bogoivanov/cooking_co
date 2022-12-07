from django.contrib.auth import get_user_model
from django.db import models

from cooking_co.cocktails.models import Cocktail

UserModel = get_user_model()


class CocktailComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    cocktail = models.ForeignKey(
        Cocktail,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    class Meta:
        ordering = ['-publication_date_and_time', ]


class CocktailLike(models.Model):
    # Photo's field for likes is named `{NAME_OF_THIS_MODEL.lower()}_set`

    cocktail = models.ForeignKey(
        Cocktail,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
