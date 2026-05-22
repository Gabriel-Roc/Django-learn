from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoItem, ToDoList
from .forms import CreateNewList, CreateNewItem
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'app_test/home.html')

@login_required
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
        if request.POST.get('deleteItem'):
            for i in lists:
                if request.POST.get('deleteItem') == str(i.id): # value in html is as a STRING
                    i.delete()
                    return redirect('/lists')
    return render(request, 'app_test/list.html', {'items': items, 'lists': lists, 'form_item': form_item})

@login_required
def new_list(request):
    if request.method == 'POST':
        form_list = CreateNewList(request.POST)
        if form_list.is_valid():
            l = ToDoList() # to do list that is on models.py, "name" and "user" are both fields on that model
            l.user = request.user
            l.name = form_list.cleaned_data['name'] # inside brackets is "name" on form, not on model
            l.save()
            '''
            i need to call in the form and then add that into the specific model field
            THEN save the model
            '''
            return redirect('/lists')
    else:
        form_list = CreateNewList()
    return render(request, 'app_test/new_list.html', {'form_list': form_list})

def invalid_user(request):
    if request.user.is_authenticated:
        return redirect('/home')
    return render(request, 'app_test/invalid_user.html')
