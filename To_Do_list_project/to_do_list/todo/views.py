from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo
from .forms import ToDoForm

# Create your views here.
def todo_list(request):
    todos = ToDo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
    else:
        form = ToDoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
    else:
        form = ToDoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo-list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})
