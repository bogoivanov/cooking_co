from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from cooking_co.common.forms import RecipeCommentForm
from cooking_co.common.models import RecipeComment, RecipeLike
from cooking_co.recipes.forms import RecipeCreateForm, RecipeEditForm
from cooking_co.recipes.models import Recipe

UserModel = get_user_model()


class RecipesViewListView(LoginRequiredMixin, ListView):
    paginate_by = 3
    context_object_name = 'recipes'
    model = Recipe
    template_name = 'recipes/recipes-all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes_count'] = self.object_list.all().count()
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'recipes/create-recipe.html'
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('recipes all')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class RecipeEditView(LoginRequiredMixin, UpdateView):
    template_name = 'recipes/recipe-edit.html'
    model = Recipe
    form_class = RecipeEditForm
    context_object_name = 'recipe'

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
