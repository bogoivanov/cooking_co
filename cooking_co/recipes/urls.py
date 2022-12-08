from django.urls import path

from cooking_co.recipes.views import recipes_all

urlpatterns = [
    path('', recipes_all, name='recipes list'),

]