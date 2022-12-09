from django import forms
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from cooking_co.accounts.helpers.get_age import get_age_profile
from cooking_co.cocktails.forms import CocktailCreateForm, CocktailLittleBaseForm
from cooking_co.cocktails.models import Cocktail
from cooking_co.common.forms import CocktailCommentForm, RecipeCommentForm
from cooking_co.common.models import CocktailComment, CocktailLike, RecipeComment, RecipeLike
from cooking_co.recipes.forms import RecipeCreateForm
from cooking_co.recipes.models import Recipe

UserModel = get_user_model()


class RecipesViewListView(LoginRequiredMixin, views.ListView):
    paginate_by = 5
    context_object_name = 'recipes'  # renames `object_list` to `employees`
    model = Recipe
    template_name = 'recipes/recipes-all.html'  # web/employee_list.html




class RecipeCreateView(CreateView):
    template_name = 'recipes/create-recipe.html'
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('recipes all')
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class RecipeEditView(UpdateView):
    template_name = 'recipes/recipe-edit.html'
    model = Recipe
    context_object_name = 'recipe'
    fields = ('recipe_name', 'main_ingredient', 'other_ingredient', 'recipe_photo')

    def get_success_url(self):
        return reverse_lazy('recipe details', kwargs={
            'slug': self.object.slug,
        })


class RecipeDetailView(DetailView):
    template_name = 'recipes/recipe-details.html'
    model = Recipe
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object
        recipe_liked = RecipeLike.objects.filter(recipe_id=recipe.pk, user_id=self.request.user.pk)
        context['user_liked_recipe'] = recipe_liked
        context['recipe_likes_count'] = len(self.object.recipelike_set.all())
        context['comments'] = self.object.recipecomment_set.all()
        context['form'] = RecipeCommentForm
        context['is_owner'] = self.request.user.pk == self.object.user_id
        return context



class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe-delete.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        RecipeComment.objects.filter(recipe_id=self.object.id).delete()
        RecipeLike.objects.filter(recipe_id=self.object.id).delete()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
