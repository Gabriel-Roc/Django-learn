from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem, ToDoList
from .forms import CreateNewList, CreateNewItem

def home(request):
    return render(request, 'home.html')

def view_list(request):
    items = ToDoItem.objects.all()
    lists = ToDoList.objects.all()
    form_item = CreateNewItem()
    if request.method == 'POST':
        if request.POST.get('save'):
            for item in items:
                if request.POST.get(str(item.id)) == "clicked":
                    item.completed = True
                else:
                    item.completed = False
                item.save()
        elif request.POST.get('saveItem'):
            form_item = CreateNewItem(request.POST)
            if form_item.is_valid():
                i = form_item.cleaned_data['text']
                l = form_item.cleaned_data['todo_list']
                t = ToDoItem(text=i, todo_list=l) # to do item that is on models.py
                t.save()
    return render(request, 'list.html', {'items': items, 'lists': lists, 'form_item': form_item})

def new_list(request):
    if request.method == 'POST':
        form_list = CreateNewList(request.POST)
        if form_list.is_valid():
            l = form_list.cleaned_data['name']
            t = ToDoList(name=l) # to do list that is on models.py
            t.save()
    else:
        form_list = CreateNewList()
    return render(request, 'new_list.html', {'form_list': form_list})