from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from cooking_co.cocktails.forms import CocktailCreateForm
from cooking_co.cocktails.models import Cocktail
from cooking_co.common.forms import CocktailCommentForm
from cooking_co.common.models import CocktailComment, CocktailLike

UserModel = get_user_model()


class CocktailsViewListView(LoginRequiredMixin, ListView):
    paginate_cocktails_by = 3
    model = Cocktail
    template_name = 'cocktails/cocktails-all.html'

    def get_paginated_cocktails(self):
        page = self.request.GET.get('page', 1)
        age_of_user = self.request.user.age
        if age_of_user < 21:
            cocktails = self.object_list.filter(main_ingredient='non-alcoholic')
            paginator = Paginator(cocktails, self.paginate_cocktails_by)
            return paginator.get_page(page)
        else:
            cocktails = self.object_list.all()
            paginator = Paginator(cocktails, self.paginate_cocktails_by)
            return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        age_of_user = self.request.user.age
        if age_of_user < 21:
            context['cocktails_count'] = self.object_list.filter(main_ingredient='non-alcoholic').count()
            context['cocktails'] = self.get_paginated_cocktails()
        else:
            context['cocktails_count'] = self.object_list.all().count()
            context['cocktails'] = self.get_paginated_cocktails()

        return context



class CocktailCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cocktails/create-cocktail.html'
    form_class = CocktailCreateForm
    success_url = reverse_lazy('cocktails all')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class CocktailEditView(LoginRequiredMixin, UpdateView):
    template_name = 'cocktails/cocktail-edit.html'
    model = Cocktail
    context_object_name = 'cocktail'
    fields = ('cocktail_name', 'main_ingredient', 'other_ingredient', 'cocktail_photo')

    def get_success_url(self):
        return reverse_lazy('cocktail details', kwargs={
            'slug': self.object.slug,
        })


class CocktailDetailView(DetailView):
    template_name = 'cocktails/cocktail-details.html'
    model = Cocktail
    context_object_name = 'cocktail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cocktail = self.object
        cocktail_liked = CocktailLike.objects.filter(cocktail_id=cocktail.pk, user_id=self.request.user.pk)
        context['user_liked_cocktail'] = cocktail_liked
        context['cocktail_likes_count'] = len(self.object.cocktaillike_set.all())
        context['comments'] = self.object.cocktailcomment_set.all()
        context['form'] = CocktailCommentForm
        context['is_owner'] = self.request.user.pk == self.object.user_id
        return context


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
