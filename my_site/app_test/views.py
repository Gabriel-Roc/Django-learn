from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem, ToDoList

def home(request):
    return render(request, 'home.html')

def view_list(request):
    items = ToDoItem.objects.all()
    lists = ToDoList.objects.all()
    return render(request, 'list.html', {'items': items, 'lists': lists})