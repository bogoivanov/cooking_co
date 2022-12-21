from cloudinary.forms import CloudinaryFileField

from cooking_co.cocktails.models import Cocktail

from django import forms


class CocktailBaseForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = ('cocktail_name', 'main_ingredient', 'other_ingredient','prepare', 'cocktail_photo')
        labels = {
            'recipe_name': 'Recipe name',
            'main_ingredient': 'Main ingredient',
            'other_ingredient': 'Other ingredients',
            'recipe_photo': 'Recipe photo',
        }

        widgets = {
            'cocktail_name': forms.TextInput(
                attrs={
                    'placeholder': 'recipe name'
                }
            ),
            'other_ingredient': forms.TextInput(
                attrs={
                    'placeholder': 'other ingredients',
                }
            ),
            'prepare': forms.Textarea(
                attrs={
                    'cols': 31,
                    'rows': 4,
                    'placeholder': 'How to prepare...'
                },
            ),
        }


class CocktailLittleBaseForm(CocktailBaseForm):
    pass


class CocktailCreateForm(CocktailBaseForm):
    pass


class CocktailEditForm(CocktailBaseForm):
    disabled_fields = ('cocktail_name',)
