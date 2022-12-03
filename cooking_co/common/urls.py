from django.urls import path, include

from cooking_co.common.views import IndexViewListView

urlpatterns = [
    path('', IndexViewListView.as_view(), name='index'),

]
