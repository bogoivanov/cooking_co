from django import forms

from cooking_co.common.models import CocktailComment, RecipeComment


class CocktailCommentForm(forms.ModelForm):
    class Meta:
        model = CocktailComment
        fields = ('text',)
        labels = {
            'text': "",
        }
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 37,
                    'rows': 2,
                    'placeholder': 'Enter comment for cocktail...'
                },
            ),
        }

class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ('text',)
        labels = {
            'text': "",
        }
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 37,
                    'rows': 2,
                    'placeholder': 'Enter comment for recipe...'
                },
            ),
        }