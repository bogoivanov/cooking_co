from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from cooking_co.accounts.helpers.get_age import get_age_profile
from cooking_co.cocktails.forms import CocktailCreateForm
from cooking_co.cocktails.models import Cocktail
from cooking_co.common.forms import CocktailCommentForm
from cooking_co.common.models import CocktailComment, CocktailLike

UserModel = get_user_model()


class CocktailsViewListView(LoginRequiredMixin, views.ListView):
    paginate_by = 5
    context_object_name = 'cocktails'  # renames `object_list` to `employees`
    model = Cocktail
    template_name = 'cocktails/cocktails-all.html'  # web/employee_list.html


class CocktailCreateView(CreateView):
    template_name = 'cocktails/create-cocktail.html'
    form_class = CocktailCreateForm
    success_url = reverse_lazy('cocktails all')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class CocktailEditView(UpdateView):
    template_name = 'cocktails/cocktail-edit.html'
    model = Cocktail
    context_object_name = 'cocktail'
    fields = ('cocktail_name', 'main_ingredient', 'other_ingredient', 'cocktail_photo')
    success_url = reverse_lazy('cocktails all')

    # def get_success_url(self):
    #     return reverse_lazy('cocktail details', kwargs={
    #         'cocktail_slug': self.slug,
    #     })
class CocktailDetailView(DetailView):
    template_name = 'cocktails/cocktail-details.html'
    model = Cocktail
    context_object_name = 'cocktail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cocktail = self.object
        cocktail_liked = CocktailLike.objects.filter(cocktail_id=cocktail.pk, user_id=self.request.user.pk)
        context['user_liked_cocktail'] = cocktail_liked
        context['cocktail_likes_count'] = len(self.object.cocktaillike_set.all()) or "0"
        context['comments'] = self.object.cocktailcomment_set.all() or None
        context['form'] = CocktailCommentForm
        context['is_owner'] = self.request.user.pk == self.object.user_id
        return context
        # cocktail_liked = CocktailLike.objects.filter(cocktail__user_id__in=CocktailLike.objects.all())
        # .prefetch_related('photolike_set')
        # context['pets_count'] = self.object.pet_set.count()
        # photos = self.object.photo_set \
        #     .prefetch_related('photolike_set')
        # context['photos_count'] = photos.count()
        # context['likes_count'] = sum(x.photolike_set.count() for x in photos)


class CocktailDeleteView(LoginRequiredMixin, DeleteView):
    model = Cocktail
    template_name = 'cocktails/cocktail-delete.html'
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        CocktailComment.objects.filter(cocktail_id=self.object.id).delete()
        CocktailLike.objects.filter(cocktail_id=self.object.id).delete()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


    #
    #
    #     login(self.request, self.object)
    #     return result
    #
    # def save(self, commit=True):
    #     print(self.object.id)
    #     print('sffssffsfdaafs')
    #     if commit:
    #         self.object.tagged_pets.clear()  # many-to-many
    #         # Cocktail.objects.all() \
    #         #     .first().tagged_pets.clear()
    #         # CocktailLike.objects.filter(photo_id=self.instance.id) \
    #         #     .delete()  # one-to-many
    #         CocktailComment.objects.filter(cocktail_id=self.object.id) \
    #             .delete()
    #         print(CocktailComment.objects.filter(cocktail_id=self.object.id))
    #         # CocktailComment.objects.filter(user_id=self.instance.id) \
    #         #     .delete()
    #         # one-to-many
    #         self.object.delete()
    #
    #     return self.object
    #
    #     login(self.request, self.object)
    #     return result
