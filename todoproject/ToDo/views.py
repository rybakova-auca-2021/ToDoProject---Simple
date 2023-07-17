from django.shortcuts import render
from .models import ToDoItem
from django.http import HttpResponseRedirect 

def toDoAppView(request):
    all_todo_items = ToDoItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items}) 

def addToDoView(request):
    x = request.POST['content']
    new_item = ToDoItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/list/') 