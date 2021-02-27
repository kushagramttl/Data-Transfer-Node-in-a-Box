from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Containers
import uuid

# Create your views here.
def index(request):
    return render(request, 'portal/index.html', {})

def register(request):
    container_id = str(uuid.uuid4())
    username = QueryDict(request.get_full_path().split("?")[1])["user"]
    user = User.objects.get(username=username)
    Containers.objects.create(container_id=container_id, user=user)
    return JsonResponse({'c_id': container_id})

    # return HttpResponse("Welcome to the Portal " + container_id)
