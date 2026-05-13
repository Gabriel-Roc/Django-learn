from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class ToDoItem(models.Model):
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text