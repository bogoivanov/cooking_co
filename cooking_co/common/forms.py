from django import forms

from cooking_co.common.models import CocktailComment, RecipeComment
from cooking_co.common.core.dirty_words_validator import validate_dirty_words


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
                    'cols': 47,
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
                    'cols': 47,
                    'rows': 2,
                    'placeholder': 'Enter comment for recipe...'
                },
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        validate_dirty_words(cleaned_data['text'])



