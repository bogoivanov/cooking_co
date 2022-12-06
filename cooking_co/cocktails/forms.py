from cooking_co.cocktails.models import Cocktail

from django import forms


# from petstagram.core.form_mixins import DisabledFormMixin
# from petstagram.pets.models import Pet


# `ModelForm` and `Form`:
# - `ModelForm` binds to models
# - `Form` is detached from models

class CocktailBaseForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        # fields = '__all__' (not the case, we want to skip `slug`
        fields = ('cocktail_name', 'main_ingredient', 'other_ingredient', 'cocktail_photo')
        # exclude = ('slug',)
        # labels = {
        #     'cocktail_name': 'Cocktail name',
        #     'cocktail_photo': 'Cocktail photo',
        #     'main_ingredient': 'Main ingredient',
        # }
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Cocktail name'
        #         }
        #     ),
        #     'main_ingredient': forms.TextInput(
        #         attrs={
        #             'main_ingredient': 'choose',
        #         }
        #     ),
        #     'cocktail_photo': forms.URLInput(
        #         attrs={
        #             'placeholder': 'Link to image',
        #         }
        #     )
        # }


class CocktailCreateForm(CocktailBaseForm):
    pass


class CocktailEditForm(CocktailBaseForm):
    disabled_fields = ('cocktail_name',)


class CocktailDeleteForm(CocktailBaseForm):
    disabled_fields = ('cocktail_name', 'main_ingredient', 'cocktail_photo')
