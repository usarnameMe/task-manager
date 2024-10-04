from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
import json


class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks_to_do'] = Task.objects.filter(status='To Do')
        context['tasks_in_progress'] = Task.objects.filter(status='In Progress')
        context['tasks_review'] = Task.objects.filter(status='Review')
        context['tasks_done'] = Task.objects.filter(status='Done')
        return context


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'status', 'priority', 'deadline']
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'status', 'priority', 'deadline']
    template_name = 'task/task_update.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')


def update_task_status(request, task_id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(pk=task_id)
            data = json.loads(request.body)
            new_status = data.get('status')

            if new_status in dict(Task.STATUS_CHOICES):
                task.status = new_status
                task.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid status provided'})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
