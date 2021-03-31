from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('autherror/', views.auth_error, name='autherror'),
    path('signout/', views.signout, name='signout'),
    path('register/', views.register, name='index'),
    path('containers/', views.containers, name='index'),
    path('commands/', views.commands, name='index'),
    path('commands/<id>', views.commands, name='index'),
    path('transfers/<id>', views.transfers, name='index'),
    path('transfers/', views.transfers, name='index'),
    path('create-command/', views.create_command, name='index'),
    path('', admin.site.urls),
]
