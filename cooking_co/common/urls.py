from django.urls import path, include

from cooking_co.common.views import IndexViewListView, CocktailsSearchListView, users_list, comment_cocktail, like_cocktail, TestViewListView

urlpatterns = [
    path('', IndexViewListView.as_view(), name='index'),
    path('search-cocktails/', CocktailsSearchListView.as_view(), name='cocktails search'),
    path('users/', users_list, name='all users'),
    # path('like-post/<int:post_pk>', like_post, name='like post'),
    path('create-comment/<int:cocktail_id>/', comment_cocktail, name='comment cocktail'),
    path('like-cocktail/<int:cocktail_id>/', like_cocktail, name='like cocktail'),
    # path('users/', UsersViewListView.as_view(), name='all users')
    path('test/',TestViewListView.as_view() , name='all users'),
]
