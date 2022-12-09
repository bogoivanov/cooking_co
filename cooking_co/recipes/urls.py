from django.urls import path, include


from cooking_co.recipes.views import RecipesViewListView, RecipeCreateView, RecipeDetailView, RecipeEditView, \
    RecipeDeleteView

urlpatterns = [
    path('all_recipes/', RecipesViewListView.as_view(), name='recipes all'),
    path('add-recipe/', RecipeCreateView.as_view(), name='recipe create'),
    path('/<slug:slug>/', include([
        path('redipe-details/', RecipeDetailView.as_view(), name='recipe details'),
        path('redipe-edit/', RecipeEditView.as_view(), name='recipe edit'),
        path('redipe-delete/', RecipeDeleteView.as_view(), name='recipe delete'),
    ]))
]