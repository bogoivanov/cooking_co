from django.urls import path, include

from cooking_co.common.views import IndexViewListView, CocktailsSerchListView, users_list

urlpatterns = [
    path('', IndexViewListView.as_view(), name='index'),
    path('search-cocktails/', CocktailsSerchListView.as_view(), name='cocktails search'),
    path('users/', users_list, name='all users'),
    # path('users/', UsersViewListView.as_view(), name='all users')
]
