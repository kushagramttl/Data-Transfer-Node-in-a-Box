from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('register/', views.register, name='index'),
    path('containers/', views.containers, name='index'),
    path('commands/', views.commands, name='index'),
    path('create-command/', views.create_command, name='index'),
    path('', admin.site.urls),
]
