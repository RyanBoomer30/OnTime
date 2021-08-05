from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import datetime

class User(AbstractUser):
    pass

class Project(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user")
    projects = models.ManyToManyField('Task', related_name="task", blank=True)
    name = models.CharField(max_length=200, default="New Task")

    def __str__(self):
        return f"{self.user} created project {self.name}"

class Task(models.Model):
    title = models.CharField(max_length=200, default="New Task")
    todo = models.ManyToManyField('List', related_name="list", blank=True)
    time = models.DateTimeField(default=datetime.now().strftime(("%Y-%m-%d"))) 

    def __str__(self):
        return f"{self.title} created a task at {self.time}"

class List(models.Model):
    content = models.CharField(max_length=200, default="New List")
    status = models.BooleanField(default=True)
    createdTime = models.DateTimeField(default=datetime.now().strftime(("%Y-%m-%d"))) 

    def __str__(self):
        return f"{self.content} has a status {self.status}"