from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.welcome, name='index'),
    path('login/', admin.site.urls),
]
