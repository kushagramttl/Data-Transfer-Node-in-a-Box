from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Container, Command
from django.contrib.auth import authenticate, login, logout

import uuid

# Create your views here.
def signin(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'portal/index.html', {})
    else:
        return HttpResponse("Login Error! Try again!")


def register(request):
    if request.user.is_authenticated:
        container_id = str(uuid.uuid4())
        # username = QueryDict(request.get_full_path().split("?")[1])["user"]
        user = User.objects.get(id=request.user.id)
        Container.objects.create(container_id=container_id, user=user)
        return JsonResponse({'c_id': container_id})
    else:
        return HttpResponse("Please login")


def signout(request):
    logout(request)
    return HttpResponse("Successfully logged Out !")


def receive(request):
    if request.user.is_authenticated:
        command_id = str(uuid.uuid4())
        container_id = request.GET["container_id"]
        container = Container.objects.get(container_id=container_id)
        Command.objects.create(command_id=command_id, sender=container)
        return JsonResponse({'command_created': "true"})
    else:
        return HttpResponse("Please login")
