from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'date_of_birth',)
        field_classes = {'email': auth_forms.UsernameField}
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                },
            ),
        }


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'gender', 'profile_image',)

    widgets = {
        'first_name': forms.TextInput(
            attrs={
                'placeholder': 'first name',
            },
        ),
        'last_name': forms.TextInput(
            attrs={
                'placeholder': 'last name',
            },
        ),
        'gender': forms.Select(),
    }

