from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from cooking_co.cocktails.models import Cocktail
from cooking_co.common.decorators import allow_groups
from cooking_co.common.forms import CocktailCommentForm, RecipeCommentForm
from cooking_co.common.models import CocktailLike, RecipeLike
from cooking_co.recipes.models import Recipe

UserModel = get_user_model()


@login_required
def comment_cocktail(request, cocktail_id):
    cocktail = Cocktail.objects.filter(id=cocktail_id).get()
    form = CocktailCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.cocktail = cocktail
        comment.user = request.user
        comment.save()

    return redirect(request.META['HTTP_REFERER'])


@login_required
def like_cocktail(request, cocktail_id):
    user_liked_photos = CocktailLike.objects.filter(cocktail_id=cocktail_id, user_id=request.user.pk)
    cocktail = Cocktail.objects.filter(id=cocktail_id).first()

    user_is_owner = cocktail.user.id == request.user.pk

    if user_is_owner:
        return redirect(request.META['HTTP_REFERER'])
    elif user_liked_photos:
        user_liked_photos.delete()
    else:
        CocktailLike.objects.create(cocktail_id=cocktail_id, user_id=request.user.pk, )

    return redirect(request.META['HTTP_REFERER'])


@login_required
def comment_recipe(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).get()
    form = RecipeCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.recipe = recipe
        comment.user = request.user
        comment.save()

    return redirect(request.META['HTTP_REFERER'])


@login_required
def like_recipe(request, recipe_id):
    user_liked_photos = RecipeLike.objects.filter(recipe_id=recipe_id, user_id=request.user.pk)
    recipe = Recipe.objects.filter(id=recipe_id).first()

    user_is_owner = recipe.user.id == request.user.pk

    if user_is_owner:
        return redirect(request.META['HTTP_REFERER'])
    elif user_liked_photos:
        user_liked_photos.delete()
    else:
        RecipeLike.objects.create(recipe_id=recipe_id, user_id=request.user.pk, )

    return redirect(request.META['HTTP_REFERER'])


class TestViewListView(LoginRequiredMixin, ListView):
    model = UserModel
    context_object_name = 'profile'
    template_name = 'common/test.html'


class Test404View(TemplateView):
    template_name = '404/404.html'


class IndexViewListView(ListView):
    model = UserModel
    context_object_name = 'profile'
    template_name = 'common/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['alcoholic_cocktails'] = Cocktail.objects.exclude(main_ingredient='non-alcoholic').count()
        context['non_alcoholic_cocktails'] = Cocktail.objects.filter(main_ingredient='non-alcoholic').count()
        context['all_cocktails'] = Cocktail.objects.all().count()
        context['all_recipes'] = Recipe.objects.all().count()
        context['all_articles'] = Cocktail.objects.all().count() + Recipe.objects.all().count()
        if self.request.user.is_anonymous:
            context['age_of_user'] = 16
        else:
            context['age_of_user'] = self.request.user.age
        context['all_articles_without_alcohol'] = Cocktail.objects.filter(
            main_ingredient='non-alcoholic').count() + Recipe.objects.all().count()
        return context


class CocktailsSearchListView(LoginRequiredMixin, ListView):
    model = Cocktail
    context_object_name = 'cocktails'
    template_name = 'common/search-cocktails.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.__get_pattern()
        if self.request.user.age < 21:
            queryset = queryset.filter(main_ingredient__icontains='non-alcoholic')
        if pattern:
            search_by_name_cocktail = queryset.filter(cocktail_name__icontains=pattern)
            search_by_main_ingredient_cocktail = queryset.filter(main_ingredient__icontains=pattern)
            queryset = search_by_name_cocktail | search_by_main_ingredient_cocktail
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class RecipesSearchListView(LoginRequiredMixin, ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'common/search-recipes.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.__get_pattern()
        if pattern:
            search_by_name_recipe = queryset.filter(recipe_name__icontains=pattern)
            search_by_main_ingredient_recipe = queryset.filter(main_ingredient__icontains=pattern)
            queryset = search_by_name_recipe | search_by_main_ingredient_recipe
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


@allow_groups(groups=['StaffCC'])
def users_list(request):
    users = UserModel.objects.all()
    context = {
        'users': users,
    }

    return render(request, 'common/users.html', context, )
