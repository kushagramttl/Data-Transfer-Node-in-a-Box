from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Container, Command, Transfer
from django.contrib.auth import authenticate, login, logout
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
import json
import uuid

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/portal/containers/')
    else:
        form = UserCreationForm()
    return render(request, 'portal/signup.html', {'form': form})


def signin(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        data = Container.objects.filter(user=user)
        return render(request, 'portal/index.html', {'data': data})
    else:
        return HttpResponse("Login Error! Try again!")


def auth_error(request):
    return HttpResponse("Please login")


@login_required(login_url='/portal/autherror/')
def containers(request):
    data = Container.objects.filter(user=request.user)
    return render(request, 'portal/index.html', {'data': data})


@login_required(login_url='/portal/autherror/')
def register(request):
    data = json.loads(request.body.decode("utf-8"))
    container_id = str(uuid.uuid4())
    user = User.objects.get(id=request.user.id)
    access_key = data['access_key']
    secret_key = data['secret_key']
    port = data['port']
    ip_address = data['ip_address']
    Container.objects.create(container_id=container_id, user=user, access_key=access_key,
                             secret_key=secret_key, port=port, ip_address=ip_address)
    return JsonResponse({'c_id': container_id})


def signout(request):
    logout(request)
    return HttpResponse("Successfully logged Out !")


@login_required(login_url='/portal/autherror/')
def commands(request, id=None):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        command_id = str(uuid.uuid4())
        access_key = request.POST['access_key']
        secret_key = request.POST['secret_key']
        port = request.POST['port']
        ip_address = request.POST['ip_address']
        Command.objects.create(command_id=command_id, sender=user, access_key=access_key,
                               secret_key=secret_key, port=port, ip_address=ip_address)
        return JsonResponse({'command_id': command_id})
    elif request.method == "GET":
        qs = Command.objects.filter(sender=user)
        data = serialize("json", qs, fields=(
            "access_key", "secret_key", "ip_address", "port"))
        return HttpResponse(data, content_type="application/json")
    elif request.method == "DELETE":
        commands = Command.objects.filter(command_id=id)
        count = commands.count()
        if(count > 0):
            Command.objects.filter(command_id=id).delete()
            return JsonResponse({'deleted': "true"})

        else:
            return JsonResponse({'deleted': "false"})


@login_required(login_url='/portal/autherror/')
def create_command(request):
    return render(request, 'portal/create_command.html', {})


@login_required(login_url='/portal/autherror/')
def transfers(request, id=None):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        Transfer.objects.create(transfer_id=id, sender=user, status="Started")
        return JsonResponse({'transfer_created': "true"})
    elif request.method == "PUT":
        status = json.loads(request.body.decode("utf-8"))['status']
        Transfer.objects.filter(transfer_id=id).update(status=status)
        return JsonResponse({'transfer_updated': "true"})
    elif request.method == "GET":
        qs = Transfer.objects.filter(sender=user)
        data = serialize("json", qs, fields=(
            "access_key", "secret_key", "ip_address", "port"))
        return HttpResponse(data, content_type="application/json")


@login_required(login_url='/portal/autherror/')
def view_transfers(request):
    data = Transfer.objects.filter(sender=request.user)
    return render(request, 'portal/transfers.html', {'data': data})
