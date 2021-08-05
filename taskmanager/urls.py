from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createProject", views.createProject, name="createProject"),
    path("viewProject/<int:project_id>", views.viewProject, name="viewProject"),
    path("deleteProject/<int:project_id>", views.deleteProject, name="deleteProject"),
    path("createTask/<int:project_id>", views.createTask, name="createTask"),
    path("editTask/<int:project_id>/<int:task_id>", views.editTask, name="editTask"),
    path("deleteTask/<int:project_id>/<int:task_id>", views.deleteTask, name="deleteTask"),
    path("createList/<int:project_id>/<int:task_id>", views.createList, name="createList"),
    path("editList/<int:project_id>/<int:task_id>/<int:list_id>", views.editList, name="editList"),
    path("deleteList/<int:project_id>/<int:task_id>/<int:list_id>", views.deleteList, name="deleteList"),
    path("toggleList/<int:project_id>/<int:task_id>/<int:list_id>", views.toggleList, name="toggleList"),
]
