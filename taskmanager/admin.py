from django.contrib import admin

# Register your models here.
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("__str__")

class TaskAdmin(admin.ModelAdmin):
    list_display = ("__str__")

class ListAdmin(admin.ModelAdmin):
    list_display = ("__str__")

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(List)