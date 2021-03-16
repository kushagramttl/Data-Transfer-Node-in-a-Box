from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Container, Command
from django.contrib.auth import authenticate, login, logout
from django.core.serializers import serialize

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
        access_key = request.POST['access_key']
        secret_key = request.POST['secret_key']
        port = request.POST['port']
        ip_address = request.POST['ip_address']
        Container.objects.create(container_id=container_id, user=user, access_key=access_key,
                                 secret_key=secret_key, port=port, ip_address=ip_address)
        return JsonResponse({'c_id': container_id})
    else:
        return HttpResponse("Please login")


def signout(request):
    logout(request)
    return HttpResponse("Successfully logged Out !")


def commands(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            command_id = str(uuid.uuid4())
            # container_id = request.GET["container_id"]
            # container = Container.objects.get(container_id=container_id)
            user = User.objects.get(id=request.user.id)
            access_key = request.POST['access_key']
            secret_key = request.POST['secret_key']
            port = request.POST['port']
            ip_address = request.POST['ip_address']
            Command.objects.create(command_id=command_id, sender=user, access_key=access_key,
                                   secret_key=secret_key, port=port, ip_address=ip_address)
            return JsonResponse({'command_created': "true"})
        elif request.method == "GET":
            return HttpResponse([], content_type="application/json")
    else:
        return HttpResponse("Please login")


def create_command(request):
    if request.user.is_authenticated:
        return render(request, 'portal/create_command.html', {})
    else:
        return HttpResponse("Please login")
