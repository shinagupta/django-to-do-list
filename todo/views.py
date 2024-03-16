from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request, "index.html", { "todos": todos })

@require_http_methods(["POST"])
def create_todo(request):
    title = request.POST.get('title')
    todo = Todo.objects.create(title=title)
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})

def mark_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = True
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})
