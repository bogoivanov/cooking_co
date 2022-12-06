import pyperclip as pyperclip
from django import forms
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.shortcuts import render, redirect

from cooking_co.cocktails.models import Cocktail
from cooking_co.common.decorators import allow_groups

UserModel = get_user_model()



# def like_photo(request, photo_id):
#     user_liked_photos = PhotoLike.objects \
#         .filter(photo_id=photo_id, user_id=request.user.pk)
#
#     if user_liked_photos:
#         user_liked_photos.delete()
#     else:
#         PhotoLike.objects.create(
#             photo_id=photo_id,
#             user_id=request.user.pk,
#         )
#
#     return redirect(get_photo_url(request, photo_id))
#
def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
    })
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))

#
# @login_required
# def comment_photo(request, photo_id):
#     photo = Photo.objects.filter(pk=photo_id) \
#         .get()
#
#     form = PhotoCommentForm(request.POST)
#
#     if form.is_valid():
#         comment = form.save(commit=False)  # Does not persist to DB
#         comment.photo = photo
#         comment.save()
#
#     return redirect('index')



class IndexViewListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    context_object_name = 'profile'
    template_name = 'common/index.html'


class CocktailsSerchListView(auth_mixins.LoginRequiredMixin, views.ListView):
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


@allow_groups(groups=['Users statistics'])
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
