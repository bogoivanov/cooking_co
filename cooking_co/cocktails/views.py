from django.contrib.auth import get_user_model, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model

from cooking_co.accounts.helpers.get_age import get_age_profile
from cooking_co.cocktails.forms import CocktailCreateForm
from cooking_co.cocktails.models import Cocktail

UserModel = get_user_model()


class CocktailsViewListView(views.ListView):
    paginate_by = 4
    context_object_name = 'cocktails'  # renames `object_list` to `employees`
    model = Cocktail
    template_name = 'cocktails/cocktails-all.html'  # web/employee_list.html
    extra_context = {'title': 'List view'}  # static context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.__get_pattern()
        if pattern:
            queryset = queryset.filter(last_name__icontains=pattern)
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class CocktailCreateView(views.CreateView):
    template_name = 'cocktails/create-cocktail.html'
    form_class = CocktailCreateForm
    success_url = reverse_lazy('cocktails all')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class CocktailEditView(views.UpdateView):
    template_name = 'cocktails/cocktail-edit.html'
    model = Cocktail
    context_object_name = 'cocktail'
    fields = ('cocktail_name', 'main_ingredient', 'other_ingredient', 'cocktail_photo')
    success_url = reverse_lazy('cocktails all')

    # def get_success_url(self):
    #     return reverse_lazy('cocktail details', kwargs={
    #         'cocktail_slug': self.slug,
    #     })


class CocktailDetailView(views.DetailView):
    template_name = 'cocktails/cocktail-details.html'
    model = Cocktail
    context_object_name = 'cocktail'

    # user_cocktails = UserModel.cocktail_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['profile_age'] = get_age_profile(self.object.date_of_birth)
        context['is_owner'] = self.request.user.pk == self.object.user_id
        return context
        # context['pets_count'] = self.object.pet_set.count()
        # photos = self.object.photo_set \
        #     .prefetch_related('photolike_set')
        # context['photos_count'] = photos.count()
        # context['likes_count'] = sum(x.photolike_set.count() for x in photos)


class CocktailDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    fields = '__all__'
    model = Cocktail
    context_object_name = 'cocktail'
    template_name = 'cocktails/cocktail-delete.html'
    success_url = reverse_lazy('index')
