from cooking_co.cocktails.models import Cocktail

from django import forms


class CocktailBaseForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = ('cocktail_name', 'main_ingredient', 'other_ingredient', 'cocktail_photo')
        labels = {
            'cocktail_name': 'Cocktail name',
            'main_ingredient': 'Main ingredient',
            'other_ingredient': 'Other ingredients',
            'cocktail_photo': 'Cocktail photo',
        }
        widgets = {
            'cocktail_name': forms.TextInput(
                attrs={
                    'placeholder': 'cocktail name'
                }
            ),
            'other_ingredient': forms.TextInput(
                attrs={
                    'placeholder': 'other ingredients',
                }
            ),
            'cocktail_photo': forms.URLInput(
                attrs={
                    'placeholder': 'cocktail image',
                }
            )
        }


class CocktailLittleBaseForm(CocktailBaseForm):
    pass


class CocktailCreateForm(CocktailBaseForm):
    pass


class CocktailEditForm(CocktailBaseForm):
    disabled_fields = ('cocktail_name',)
