from django.urls import path

from cooking_co.common.views import IndexViewListView, CocktailsSearchListView, users_list, comment_cocktail, \
    like_cocktail, TestViewListView, comment_recipe, like_recipe, RecipesSearchListView, redirect_app_user_list

urlpatterns = [
    path('', IndexViewListView.as_view(), name='index'),
    path('', redirect_app_user_list, name='go home'),
    path('search-cocktails/', CocktailsSearchListView.as_view(), name='cocktails search'),
    path('search-recipes/', RecipesSearchListView.as_view(), name='recipes search'),

    path('cocktail/create-comment/<int:cocktail_id>/', comment_cocktail, name='comment cocktail'),
    path('cocktail/like-cocktail/<int:cocktail_id>/', like_cocktail, name='like cocktail'),

    path('recipe/create-comment/<int:recipe_id>/', comment_recipe, name='comment recipe'),
    path('recipe/like-cocktail/<int:recipe_id>/', like_recipe, name='like recipe'),

    path('users/', users_list, name='all users'),
    path('test/', TestViewListView.as_view(), name='test users'),
]
