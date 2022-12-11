from django import forms

from cooking_co.recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'main_ingredient', 'other_ingredient', 'recipe_photo')
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
            'recipe_photo': forms.URLInput(
                attrs={
                    'placeholder': 'recipe image',
                }
            )
        }
        # widgets = {
        #
        #
        #     'date_of_birth': forms.DateInput(
        #         attrs={
        #             'placeholder': 'mm/dd/yyyy',
        #             'type': 'date',
        #         },
        #     ),
        # }

        # def clean(self):
        #     cleaned_data = super().clean()
        #     print(cleaned_data)
        #     main_ingredient = cleaned_data.get('main_ingredient')
        #     self._validate_unique = True
        #     return self.cleaned_data

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


class RecipeLittleBaseForm(RecipeBaseForm):
    pass


class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeEditForm(RecipeBaseForm):
    disabled_fields = ('recipe_name',)
