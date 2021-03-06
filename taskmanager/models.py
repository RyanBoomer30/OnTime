from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Project(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user")
    projects = models.ManyToManyField('Task', related_name="task", blank=True)
    name = models.CharField(max_length=30, default="New Task")

    def __str__(self):
        return f"{self.user} created project {self.name}"

class Task(models.Model):
    title = models.CharField(max_length=30, default="New Task")
    todo = models.ManyToManyField('List', related_name="list", blank=True)
    time = models.DateTimeField(default=timezone.now()) 

    def __str__(self):
        return f"{self.title} created a task at {self.time}"

class List(models.Model):
    content = models.CharField(max_length=200, default="New List")
    status = models.BooleanField(default=True)
    createdTime = models.DateTimeField(default=timezone.now()) 

    def __str__(self):
        return f"{self.content} has a status {self.status}"