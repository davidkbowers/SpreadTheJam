"""
URL configuration for djangostj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from . import views
from .views import SearchListView

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('shows/', views.shows, name='shows'),
    path('about/', views.about, name='about'),
    path('bands/', views.bands, name='bands'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('search/', SearchListView.as_view(), name='search'),

]
