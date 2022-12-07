from django.urls import path, include

from cooking_co.cocktails.views import CocktailCreateView, CocktailsViewListView, CocktailEditView, CocktailDetailView, \
    CocktailDeleteView

urlpatterns = [
    path('all_cocktails/', CocktailsViewListView.as_view(), name='cocktails all'),
    path('add-cocktail/', CocktailCreateView.as_view(), name='cocktail create'),
    path('/<slug:slug>/', include([
        path('cocktail-details/', CocktailDetailView.as_view(), name='cocktail details'),
        path('cocktail-edit/', CocktailEditView.as_view(), name='cocktail edit'),
        path('cocktail-delete/', CocktailDeleteView.as_view(), name='cocktail delete'),
    ]))

]
