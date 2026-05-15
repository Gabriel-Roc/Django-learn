from django import forms
from .models import ToDoList

class CreateNewList(forms.Form):
    name = forms.CharField(label='List Name', max_length=200)
    completion = forms.BooleanField(label='Completion', required=False)

class CreateNewItem(forms.Form):
    todo_list = forms.ModelChoiceField(queryset=ToDoList.objects.all(), label='To-Do List')
    text = forms.CharField(label='Item Text', max_length=200)
    completed = forms.BooleanField(label='Completed', required=False)