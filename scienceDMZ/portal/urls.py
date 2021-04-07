from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('autherror/', views.auth_error, name='autherror'),
    path('signout/', views.signout, name='signout'),
    path('register/', views.register, name='register'),
    path('containers/', views.containers, name='containers'),
    path('commands/', views.commands, name='commands'),
    path('commands/<id>', views.commands, name='delete-commands'),
    path('transfers/<id>', views.transfers, name='update-transfers'),
    path('transfers/', views.transfers, name='transfers'),
    path('view-transfers/', views.view_transfers, name='view_transfers'),
    path('create-command/', views.create_command, name='create-command'),
    path('', views.signup, name='home'),
]
