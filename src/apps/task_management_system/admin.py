from django.contrib import admin

from apps.task_management_system.models import Project, Task


class TaskAdmin(admin.ModelAdmin):

    list_filter = [
        "priority",
        "status",
        "deadline",
    ]


# Register your models here.
admin.site.register(Project)
admin.site.register(Task, TaskAdmin)
