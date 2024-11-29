from django.contrib import admin

from apps.task_management_system.models import Project, Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
