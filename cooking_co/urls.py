"""cooking_co URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.urls import re_path as url

from cooking_co.common.views import PageNotFoundView

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # url(r'/admin/oauth/', include('oauthadmin.urls')),

                  path('', include('cooking_co.common.urls')),

                  path('accounts/', include('cooking_co.accounts.urls')),

                  path('recipes/', include('cooking_co.recipes.urls')),

                  path('cocktails/', include('cooking_co.cocktails.urls')),

              ] 

handler404 = PageNotFoundView.as_view()