from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem, ToDoList
from .forms import CreateNewList, CreateNewItem

def home(request):
    return render(request, 'home.html')

def view_list(request):
    items = ToDoItem.objects.all()
    lists = ToDoList.objects.all()
    return render(request, 'list.html', {'items': items, 'lists': lists})

def new_list(request):
    if request.method == 'POST':
        form_list = CreateNewList(request.POST)
        form_item = CreateNewItem(request.POST)
        if form_list.is_valid() and form_item.is_valid():
            l = form_list.cleaned_data['name']
            t = ToDoList(name=l) # to do list that is on models.py
            t.save()
            i = form_item.cleaned_data['text']
            c = ToDoItem(text=i, todo_list=t) # to do item that is on models.py
            c.save()
    else:
        form_list = CreateNewList()
        form_item = CreateNewItem()
    return render(request, 'new_list.html', {'form_list': form_list, 'form_item': form_item})