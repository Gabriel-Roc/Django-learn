from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ToDo

def home(request):
    return render(request, 'home.html')

def todos(request):
    items = ToDo.objects.all()
    return render(request, 'todos.html', {'todos': items})
