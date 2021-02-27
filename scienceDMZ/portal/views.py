from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
import uuid

# Create your views here.


def index(request):
    # result = User.objects.get(username="admin")
    # return HttpResponse(result.username)
    return render(request, 'portal/index.html', {})


def welcome(request):
    container_id =  str(uuid.uuid4())
    return JsonResponse({'c_id': container_id})

    # return HttpResponse("Welcome to the Portal " + container_id)
