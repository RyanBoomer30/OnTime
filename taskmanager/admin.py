from django.contrib import admin

# Register your models here.
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ("__str__")

class ListAdmin(admin.ModelAdmin):
    list_display = ("__str__")

admin.site.register(Task)
admin.site.register(List)