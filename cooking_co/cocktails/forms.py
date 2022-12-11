from cooking_co.cocktails.models import Cocktail

from django import forms

from cooking_co.common.models import CocktailComment
from cooking_co.core.disabled_form_mixin import DisabledFormMixin


# from petstagram.core.form_mixins import DisabledFormMixin
# from petstagram.pets.models import Pet


# `ModelForm` and `Form`:
# - `ModelForm` binds to models
# - `Form` is detached from models


class CocktailBaseForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        # fields = '__all__' (not the case, we want to skip `slug`)
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


class CocktailLittleBaseForm(CocktailBaseForm):
    pass


class CocktailCreateForm(CocktailBaseForm):
    pass


class CocktailEditForm(CocktailBaseForm):
    disabled_fields = ('cocktail_name',)

# class CocktailDeleteForm(CocktailBaseForm):
#     disabled_fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def save(self, commit=True):
#         if commit:
#             self.instance.tagged_pets.clear()  # many-to-many
#
#             Photo.objects.all() \
#                 .first().tagged_pets.clear()
#             CocktailLike.objects.filter(photo_id=self.instance.id) \
#                 .delete()  # one-to-many
#             CocktailComment.objects.filter(photo_id=self.instance.id) \
#                 .delete()  # one-to-many
#             self.instance.delete()
#
#         return self.instance


# class CocktailDeleteForm(DisabledFormMixin, CocktailBaseForm):
#     disabled_fields = '__all__'
#     print('sffssffsfdaafs')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def save(self, commit=True):
#         print(self.instance.id)
#         print('sffssffsfdaafs')
#         if commit:
#             self.instance.tagged_pets.clear()  # many-to-many
#             # Cocktail.objects.all() \
#             #     .first().tagged_pets.clear()
#             # CocktailLike.objects.filter(photo_id=self.instance.id) \
#             #     .delete()  # one-to-many
#             CocktailComment.objects.filter(cocktail_id=self.instance.id) \
#                 .delete()
#             print(CocktailComment.objects.filter(cocktail_id=self.instance.id))
#             # CocktailComment.objects.filter(user_id=self.instance.id) \
#             #     .delete()
#             # one-to-many
#             self.instance.delete()
#
#         return self.instance
# # class CocktailDeleteForm(CocktailBaseForm):
# #     disabled_fields = ('cocktail_name', 'main_ingredient', 'cocktail_photo')
