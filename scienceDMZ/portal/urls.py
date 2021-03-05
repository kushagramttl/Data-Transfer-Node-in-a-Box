from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('register/', views.register, name='index'),
    path('', admin.site.urls),
]
