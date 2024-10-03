from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from django.utils import timezone

class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'status', 'priority', 'deadline']
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('task_list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'status', 'priority', 'deadline']
    template_name = 'task/task_update.html'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
