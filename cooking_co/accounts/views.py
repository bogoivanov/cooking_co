from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth import login, get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from cooking_co.accounts.forms import UserCreateForm, UserEditForm
from cooking_co.cocktails.models import Cocktail
from cooking_co.common.models import CocktailComment, CocktailLike, RecipeComment, RecipeLike
from cooking_co.recipes.models import Recipe

UserModel = get_user_model()


class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'


class SignUpView(CreateView):
    template_name = 'accounts/sign_up.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')


class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'profiles/profile-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'profile_image')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
    #     self.fields['last_name'].widget.attrs['placeholder'] = 'last name'
    #     self.fields['gender'].widget.attrs['placeholder'] = 'gender'
    #     self.fields['profile_image'].widget.attrs['placeholder'] = 'profile_image'
    def get_success_url(self):
        return reverse_lazy('user details', kwargs={
            'pk': self.request.user.pk,
        })


class UserDetailsView(DetailView):
    template_name = 'profiles/profile-details.html'
    model = UserModel
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cocktails_count'] = Cocktail.objects.filter(user_id=self.request.user.pk).count()
        context['cocktails'] = Cocktail.objects.filter(user_id=self.request.user.pk)

        context['recipes_count'] = Recipe.objects.filter(user_id=self.request.user.pk).count()
        context['recipes'] = Recipe.objects.filter(user_id=self.request.user.pk)

        context['is_owner'] = self.request.user == self.object

        cocktails_of_user = Cocktail.objects.filter(user_id=self.request.user.pk)
        cocktail_likes_count = sum(x.cocktaillike_set.count() for x in cocktails_of_user)
        recipes_of_user = Recipe.objects.filter(user_id=self.request.user.pk)
        recipes_likes_count = sum(x.recipelike_set.count() for x in recipes_of_user)

        context['total_likes_count'] = cocktail_likes_count + recipes_likes_count
        print(context['cocktails'])
        return context


class UserDeleteView(LoginRequiredMixin, DeleteView):
    fields = '__all__'
    model = UserModel
    context_object_name = 'profile'
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        CocktailComment.objects.filter(user_id=self.object.id).delete()
        CocktailLike.objects.filter(user_id=self.object.id).delete()
        RecipeComment.objects.filter(user_id=self.object.id).delete()
        RecipeLike.objects.filter(user_id=self.object.id).delete()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class IndexViewListView(LoginRequiredMixin, ListView):
    model = UserModel
    context_object_name = 'profile'
    template_name = 'common/index.html'
