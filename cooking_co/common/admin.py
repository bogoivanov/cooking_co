from django.contrib import admin

from cooking_co.common.models import PhotoComment


# Register your models here.
@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass
