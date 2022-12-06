from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

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
        fields = '__all__'

    widgets = {
        'gender': forms.Select(),
    }
    # class Meta:
    #     model = UserModel
    #     fields = ('first_name',)
    #     field_classes = {'email': auth_forms.UsernameField}
