from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Task(models.Model):
    objects = None
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Review', 'Review'),
        ('Done', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.deadline and self.deadline < timezone.now():
            raise ValidationError('Deadline cannot be in the past.')

    def __str__(self):
        return self.title
