from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import CreateView
from .models import Task
from django.urls import reverse_lazy

# Display tasks
def task_list(request):
    tasks = Task.objects.all().order_by('id')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Toggle task status (completed/pending)
def toggle_task_status(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'status': 'success'})

# Update task order (drag-and-drop)
def update_task_order(request):
    if request.method == 'POST':
        task_order = request.POST.getlist('task_order[]')
        for idx, task_id in enumerate(task_order):
            task = Task.objects.get(id=task_id)
            task.id = idx + 1
            task.save()
        return JsonResponse({'status': 'success'})

# Create Task View
class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_create.html'  # Template for the task creation form
    fields = ['title', 'description', 'due_date']  # Adjust based on your model fields
    success_url = reverse_lazy('task-list')  # Redirect to task list after success

    def form_valid(self, form):
        # Add any additional logic here if needed
        return super().form_valid(form)
