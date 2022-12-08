
from django.contrib import admin

from cooking_co.common.models import CocktailComment, CocktailLike


# Register your models here.
@admin.register(CocktailComment)
class CommentAdmin(admin.ModelAdmin):
    pass
@admin.register(CocktailLike)
class CommentAdmin(admin.ModelAdmin):
    pass
