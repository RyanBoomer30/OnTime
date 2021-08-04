from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import *

def index(request):
    user = request.user
    if User.objects.all():
        tasks = Task.objects.filter(user=user)
        lists = dict()
        for i in tasks:
            all_list = i.todo.order_by('-createdTime')
            paginator = Paginator(all_list, 7)
            page_number = request.GET.get('page')
            lists[i.id] = paginator.get_page(page_number)
        return render(request, "taskmanager/index.html",{
            'task': tasks,
            'list': lists
        })
    else:
        return HttpResponseRedirect(reverse("login"))

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

def createTask(request):
    task = Task.objects.create(user=request.user)
    task.save()
    return HttpResponseRedirect(reverse("index"))

def editTask(request, task_id):
    task = Task.objects.get(id=task_id)
    editVersion = request.POST.get("title", "")
    task.title = editVersion
    task.save()
    return HttpResponseRedirect(reverse("index"))

def deleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse("index"))

def createList(request, task_id):
    task = Task.objects.get(id=task_id)
    default = List.objects.create()
    task.todo.add(default)
    task.save()
    return HttpResponseRedirect(reverse("index"))

def editList(request, task_id, list_id):
    task = Task.objects.get(id=task_id)
    taskList = task.todo.get(id=list_id)
    editTask = request.POST.get("title", "")
    taskList.content = editTask
    taskList.save()
    return HttpResponseRedirect(reverse("index"))

def deleteList(request, task_id, list_id):
    task = Task.objects.get(id=task_id)
    taskList = task.todo.get(id=list_id)
    taskList.delete()
    return HttpResponseRedirect(reverse("index"))


def toggleList(request, task_id, list_id):
    task = Task.objects.get(id=task_id)
    taskList = task.todo.get(id=list_id)
    if taskList.status == True:
        taskList.status = False
        taskList.save()
    else:
        taskList.status = True
        taskList.save()
    return HttpResponse(taskList.status)