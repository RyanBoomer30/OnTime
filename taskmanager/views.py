from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
import json

from .models import *

def index(request):
    user = request.user
    if user.is_anonymous:
        return HttpResponseRedirect(reverse("login"))
    else:
        project = Project.objects.filter(user=user)
        return render(request, "taskmanager/index.html",{
            'project': project,
        })

def createProject(request):
    if request.method == "POST":
        name = request.POST.get("title", "")
        project = Project.objects.create(
            user = request.user,
            name = name
        )
        project.save()
        return HttpResponseRedirect(reverse("index"))


def viewProject(request, project_id):
    user = request.user
    project = Project.objects.get(id=project_id)
    tasks = project.projects.all()
    lists = dict()

    for i in tasks:
        all_list = i.todo.order_by('-createdTime')
        paginator = Paginator(all_list, 7)
        page_number = request.GET.get('page')
        lists[i.id] = paginator.get_page(page_number)
    return render(request, "taskmanager/project.html",{
        'project_id': project_id,
        'task': tasks,
        'list': lists
    })

def deleteProject(request, project_id):
    user = request.user
    project = Project.objects.get(id=project_id)
    project.delete()
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "taskmanager/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "taskmanager/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "taskmanager/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "taskmanager/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "taskmanager/register.html")

def createTask(request, project_id):
    project = Project.objects.get(id=project_id)
    task = Task.objects.create()
    project.projects.add(task)
    project.save()
    return HttpResponseRedirect(reverse('viewProject', args=(project_id, )))

def editTask(request, project_id, task_id):
    project = Project.objects.get(id=project_id)
    task = project.projects.get(id=task_id)
    editVersion = request.POST.get("title", "")
    task.title = editVersion
    task.save()
    return HttpResponseRedirect(reverse('viewProject', args=(project_id, )))

def deleteTask(request, project_id, task_id):
    project = Project.objects.get(id=project_id)
    task = project.projects.get(id=task_id)
    task.delete()
    return JsonResponse({
        'task': "Placeholder"
    })

def createList(request, project_id, task_id):
    project = Project.objects.get(id=project_id)
    task = project.projects.get(id=task_id)
    default = List.objects.create()
    task.todo.add(default)
    task.save()
    return HttpResponseRedirect(reverse('viewProject', args=(project_id, )))

def editList(request, project_id, task_id, list_id):
    project = Project.objects.get(id=project_id)
    task = project.projects.get(id=task_id)
    taskList = task.todo.get(id=list_id)
    editTask = request.POST.get("title", "")
    taskList.content = editTask
    taskList.save()
    return HttpResponseRedirect(reverse('viewProject', args=(project_id, )))

def deleteList(request, project_id, task_id, list_id):
    project = Project.objects.get(id=project_id)
    task = project.projects.get(id=task_id)
    taskList = task.todo.get(id=list_id)
    taskList.delete()
    return JsonResponse({
        'task': "Placeholder"
    })


def toggleList(request, project_id, task_id, list_id):
    project = Project.objects.get(id=project_id)
    task = project.projects.get(id=task_id)
    taskList = task.todo.get(id=list_id)
    status = True
    if taskList.status == True:
        taskList.status = False
        taskList.save()
        status = False
    else:
        taskList.status = True
        taskList.save()
    return JsonResponse({
        'status': status
    })