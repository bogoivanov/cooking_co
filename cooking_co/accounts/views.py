from django import forms
from django.contrib.auth import forms as auth_forms, login, get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.datetime_safe import date
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django import forms
from django.contrib.auth import forms as auth_forms, login, get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from cooking_co.accounts.forms import UserCreateForm
from cooking_co.accounts.helpers.get_age import get_age_profile
from cooking_co.cocktails.models import Cocktail

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/sign_in.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/sign_up.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')



class UserEditView(views.UpdateView):
    template_name = 'profiles/profile-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'profile_image')
    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse_lazy('user details', kwargs={
            'pk': self.request.user.pk,
        })




class UserDetailsView(views.DetailView):
    template_name = 'profiles/profile-details.html'
    model = UserModel
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_age'] = get_age_profile(self.object.date_of_birth)
        # TODO
        context['cocktails_count'] = Cocktail.objects.filter(user_id=self.request.user.pk).count()
        context['cocktails'] = Cocktail.objects.filter(user_id=self.request.user.pk)
        context['is_owner'] = self.request.user == self.object
        # context['pets_count'] = self.object.pet_set.count()

        # photos = self.object.photo_set \
        #     .prefetch_related('photolike_set')

        # context['photos_count'] = photos.count()
        # context['likes_count'] = sum(x.photolike_set.count() for x in photos)
        print(context['cocktails'])
        return context


class UserDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    fields = '__all__'
    model = UserModel
    context_object_name = 'profile'
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')











class IndexViewListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    context_object_name = 'profile'
    template_name = 'common/index.html'


# class UsersViewListView(auth_mixins.LoginRequiredMixin, views.ListView):
#     model = UserModel
#     template_name = 'users.html'


#
# # Create your views here.
# class SignUpView(views.CreateView):
#     template_name = 'accounts/sign_up.html'
#     form_class = SignUpForm
#     success_url = reverse_lazy('index')
#
#     def form_valid(self, form):
#         result = super().form_valid(form)
#         login(self.request, self.object)
#         return result
#
#
# class SignInView(auth_views.LoginView):
#     template_name = 'accounts/sign_in.html'
#     success_url = reverse_lazy('index')
#
#
# class SignOutView(auth_views.LogoutView):
#     template_name = 'accounts/sign-out.html'
