from django.urls import path
from .views import task_list, toggle_task_status, update_task_order, TaskCreateView

urlpatterns = [
    path('', task_list, name='task-list'),  # Assuming this is your task list view
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),  # URL for creating a task
    path('toggle_task_status/<int:task_id>/', toggle_task_status, name='toggle-task-status'),
    path('update_task_order/', update_task_order, name='update-task-order'),
]
