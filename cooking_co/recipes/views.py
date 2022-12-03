from django.shortcuts import render

# Create your views here.
def recipes_all(request):
    return render(request, 'recipes/recipes-list.html')