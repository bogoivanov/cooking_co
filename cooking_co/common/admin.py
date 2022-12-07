
from django.contrib import admin

from cooking_co.common.models import CocktailComment

# Register your models here.
@admin.register(CocktailComment)
class CommentAdmin(admin.ModelAdmin):
    pass
