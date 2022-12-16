from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm

UserModel = get_user_model()


class UserSignInForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'email'
        self.fields['password'].widget.attrs['placeholder'] = 'password'

    class Meta:
        model = UserModel
        username = None
        fields = ('username', 'password',)


class UserCreateForm(UserCreationForm):
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


class UserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'last name'

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'gender', 'profile_image',)
