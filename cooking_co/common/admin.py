from django.contrib import admin

from cooking_co.common.models import CocktailComment, CocktailLike, RecipeComment, RecipeLike


# Register your models here.
@admin.register(CocktailComment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(CocktailLike)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeComment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeLike)
class CommentAdmin(admin.ModelAdmin):
    pass
