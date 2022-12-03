
from django import forms
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.shortcuts import render


UserModel = get_user_model()


class IndexViewListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    context_object_name = 'profile'
    template_name = 'common/index.html'


class UsersViewListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'users.html'

#
# class ProfileEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
#     fields = '__all__'
#     model = UserModel
#     context_object_name = 'profile'
#     template_name = 'profiles/profile-edit.html'
#     def get_success_url(self):
#         return reverse_lazy('profile details', kwargs={
#             'pk': self.request.user.pk,
#         })
#
# class ProfileDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):
#     model = UserModel
#     context_object_name = 'profile'
#     template_name = 'profiles/profile-details.html'
#
#
# class ProfileDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
#     fields = '__all__'
#     model = UserModel
#     context_object_name = 'profile'
#     template_name = 'profiles/profile-delete.html'
#     success_url = reverse_lazy('index')

# class IndexViewWithTemplate(views.TemplateView):
#     template_name = 'index.html'
#     extra_context = {'title': 'Template view'}
#
# class IndexViewWithTemplate(views.TemplateView):
#     template_name = 'index.html'
#     extra_context = {'title': 'Template view'}  # static context

# Dynamic context
# def get_context_data(self, **kwargs):
#     # Get `super`'s context
#     context = super().get_context_data(**kwargs)
#
#     # Add specific view stuff, one or more
#     # context['employees'] = Employee.objects.all()
#     # context['form'] = MyForm()
#
#     # Return the ready-to-use context
#     return context

# def index(request):
#     context = {
#         'title': 'FBV',
#     }
#
#     return render(request, 'index.html', context)
#
#
# class IndexView(views.View):
#     def get(self, request):
#         context = {
#             'title': 'Bare View',
#         }
#
#         return render(request, 'index.html', context)
#
#     def post(self, request):
#         pass
#
#     # In Django Rest Framework
#     # def put(self, request):
#     #     pass


# class IndexViewWithListView(views.ListView):
#     context_object_name = 'employees'  # renames `object_list` to `employees`
#     model = Employee
#     template_name = 'index.html'  # web/employee_list.html
#     extra_context = {'title': 'List view'}  # static context
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['pattern'] = self.__get_pattern()
#         return context
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#
#         pattern = self.__get_pattern()
#
#         if pattern:
#             queryset = queryset.filter(last_name__icontains=pattern)
#         return queryset
#
#     def __get_pattern(self):
#         pattern = self.request.GET.get('pattern', None)
#         return pattern.lower() if pattern else None
