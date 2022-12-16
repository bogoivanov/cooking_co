from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth import login, get_user_model
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from cooking_co import settings
from cooking_co.accounts.forms import UserCreateForm, UserEditForm, UserSignInForm
from cooking_co.cocktails.models import Cocktail
from cooking_co.common.models import CocktailComment, CocktailLike, RecipeComment, RecipeLike
from cooking_co.recipes.models import Recipe

UserModel = get_user_model()


class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'
    form_class = UserSignInForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
    form_class = UserEditForm

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
        user_names = ''
        if self.request.user.first_name and self.request.user.last_name:
            user_names = f'{self.request.user.first_name} {self.request.user.last_name}'
        elif self.request.user.first_name:
            user_names = f'{self.request.user.first_name}'
        elif self.request.user.last_name:
            user_names = f'{self.request.user.last_name}'
        context['user_names'] = user_names

        context['is_owner'] = self.request.user == self.object

        cocktails_of_user = Cocktail.objects.filter(user_id=self.request.user.pk)
        cocktail_likes_count = sum(x.cocktaillike_set.count() for x in cocktails_of_user)
        recipes_of_user = Recipe.objects.filter(user_id=self.request.user.pk)
        recipes_likes_count = sum(x.recipelike_set.count() for x in recipes_of_user)
        total_likes_count = cocktail_likes_count + recipes_likes_count
        needed_likes = max((5 - total_likes_count), 0)
        context['total_likes_count'] = total_likes_count
        context['needed_likes'] = needed_likes
        if not self.object.ready_for_moderator_email:
            if total_likes_count >= 5:
                if self.request.user == self.object:
                    self.object.ready_for_moderator = True
                    if not self.object.ready_for_moderator_email:
                        email_content = render_to_string('email_templates/moderator-greeting.html', {
                            'user': self.object})
                        user_email = self.object.email
                        send_mail(
                            subject='You are part from Cooking Coach moderators',
                            message=strip_tags(email_content),
                            html_message=email_content,
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=(user_email,),
                        )
                        self.object.ready_for_moderator_email = True
                        self.object.is_staff = True
                    group = Group.objects.get(name='ModeratorsCC')
                    self.object.groups.add(group)
                    self.object.save()
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
