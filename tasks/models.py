from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    due_datetime = models.DateTimeField(blank=True, null=True) 

    def __str__(self):
        return self.title



class Event(models.Model):
    title = models.CharField(max_length=200)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return self.title

# Create your models here.
