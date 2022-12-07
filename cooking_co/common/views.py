from django import forms
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.shortcuts import render, redirect

from cooking_co.cocktails.models import Cocktail
from cooking_co.common.decorators import allow_groups
from cooking_co.common.forms import CocktailCommentForm
from cooking_co.common.models import CocktailComment, CocktailLike

UserModel = get_user_model()


# @login_required

# def get_cocktail_url(request, cocktail_id):
#     print(request.META['HTTP_REFERER'])
#     return request.META['HTTP_REFERER'] + f'{cocktail_id}' + f'/cocktail-details/'
# http://127.0.0.1:8000/cocktails/margaritha-1/cocktail-details/
# http://127.0.0.1:8000/cocktails/margaritha-1/cocktail-details/1/cocktail-details/
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
    user_liked_photos = CocktailLike.objects \
        .filter(cocktail_id=cocktail_id, user_id=request.user.pk)
    cocktail = Cocktail.objects \
        .filter(id=cocktail_id).first()

    user_is_owner = cocktail.user.id == request.user.pk

    if user_is_owner:
        return redirect(request.META['HTTP_REFERER'])
    elif user_liked_photos:
        user_liked_photos.delete()
    else:
        CocktailLike.objects.create(
                cocktail_id=cocktail_id,
                user_id=request.user.pk,
            )
    return redirect(request.META['HTTP_REFERER'])


# class CocktailCommentCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
#     model = CocktailComment
#     form_class = CocktailCommentForm
#     success_url = reverse_lazy('index')
#     context_object_name = 'commentform'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.save()
#         return super().form_valid(form)


#


class IndexViewListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    context_object_name = 'profile'
    template_name = 'common/index.html'


class CocktailsSearchListView(auth_mixins.LoginRequiredMixin, views.ListView):
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
        if pattern:
            queryset = queryset.filter(cocktail_name__icontains=pattern)
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


# @allow_groups(groups=['Users statistics'])
def users_list(request):
    users = UserModel.objects.all()
    context = {
        'users': users,
    }

    return render(request, 'common/users.html', context, )

# @allow_groups(groups=['Staff'])
# class UsersViewListView(views.ListView):
#     model = UserModel
#     context_object_name = 'users'
#     template_name = 'common/users.html'
