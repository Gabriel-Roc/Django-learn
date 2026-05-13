from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to my site!")

def view1(request):
    return HttpResponse("This is view 1.")