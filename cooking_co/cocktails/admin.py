from django.contrib import admin

from cooking_co.cocktails.models import Cocktail


@admin.register(Cocktail)
class CocktailAdmin(admin.ModelAdmin):
    pass

    # @staticmethod
    # def pets(current_photo_obj):
    #     tagged_pets = current_photo_obj.tagged_pets.all()
    #     if tagged_pets:
    #         return ', '.join(p.name for p in tagged_pets)
    #     return 'No pets'



# @admin.register(UserModel)
# class AppUserAdmin(auth_admin.UserAdmin):
#     ordering = ('email',)
#     model = UserModel
#     list_display = ['email', 'first_name', 'last_name', 'date_of_birth', ]
#     add_fieldsets = (
#         (None, {'fields': (
#             'email', 'password1', 'password2', 'date_of_birth',)}),
#     )
#     fieldsets = (
#         (None, {
#             "fields": (
#                 ('email', 'date_of_birth', 'first_name', 'last_name', 'profile_image','gender',)
#             ),
#         }),
#         ('Permissions', {
#             'fields': ('groups', 'user_permissions'),
#         }),
#     )
#     search_fields = ('email', )
