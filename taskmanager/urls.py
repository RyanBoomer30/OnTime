from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createTask", views.createTask, name="createTask"),
    path("editTask/<int:task_id>", views.editTask, name="editTask"),
    path("deleteTask/<int:task_id>", views.deleteTask, name="deleteTask"),
    path("createList/<int:task_id>", views.createList, name="createList"),
    path("editList/<int:task_id>/<int:list_id>", views.editList, name="editList"),
    path("deleteList/<int:task_id>/<int:list_id>", views.deleteList, name="deleteList"),
    path("toggleList/<int:task_id>/<int:list_id>", views.toggleList, name="toggleList"),
]
