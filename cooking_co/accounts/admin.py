from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from cooking_co.accounts.forms import UserCreateForm, UserEditForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    model = UserModel
    list_display = ['email', 'first_name', 'last_name', 'date_of_birth', 'age']
    add_fieldsets = (
        (None, {'fields': (
            'email', 'password1', 'password2', 'date_of_birth',)}),
    )
    fieldsets = (
        (None, {
            "fields": (
                ('email', 'date_of_birth', 'first_name', 'last_name', 'profile_image','gender','age')
            ),
        }),
        ('Permissions', {
            'fields': ('groups', 'user_permissions'),
        }),
    )
    search_fields = ('email', )
    readonly_fields = (
        'age',
    )