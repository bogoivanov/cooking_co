from django import forms

from cooking_co.common.models import CocktailComment


class CocktailCommentForm(forms.ModelForm):
    class Meta:
        model = CocktailComment
        fields = ('text',)
        labels = {
            'text': "Enter comment",
        }
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 20,
                    'rows': 5,
                    'placeholder': 'Add comment...'
                },
            ),
        }
