from django import forms

from cooking_co.recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'main_ingredient', 'other_ingredient', 'prepare', 'salt','recipe_photo',)
        labels = {
            'recipe_name': 'Recipe name',
            'main_ingredient': 'Main ingredient',
            'other_ingredient': 'Other ingredients',
            'recipe_photo': 'Recipe photo',
        }

        widgets = {
            'recipe_name': forms.TextInput(
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


class RecipeLittleBaseForm(RecipeBaseForm):
    pass


class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeEditForm(RecipeBaseForm):
    disabled_fields = ('recipe_name',)
