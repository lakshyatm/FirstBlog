from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

def Todo_list(request):
    todos = Todo.objects.all()
    context={
        'Todo_list':todos
    }
    return render(request, "list.html",context)

def Todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo':todo
    }
    return render(request, "detail.html",context)

def Todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('/')
    context={
        "form": form
    }
    return render(request, "create.html",context)

def Todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None,instance=todo)
    if form.is_valid():
       form.save()
       return redirect('/')
    context={
        "form": form
    }
    return render(request, "update.html",context)

def Todo_delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')