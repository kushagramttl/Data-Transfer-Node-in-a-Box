from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<button style='margin-left: 48%; margin-top: 300px'><a href='/portal/home'>Login</a></button>")


def welcome(request):
    return HttpResponse("Welcome to the Portal")
