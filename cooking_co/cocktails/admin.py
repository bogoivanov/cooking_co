from django.contrib import admin

from cooking_co.cocktails.models import Cocktail


@admin.register(Cocktail)
class CocktailAdmin(admin.ModelAdmin):
    pass
