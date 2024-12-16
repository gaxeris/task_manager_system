from django.contrib import admin

from .models import Project, Task
from .tasks import notify_about_task_by_email


class ProjectAdmin(admin.ModelAdmin):

    list_filter = [
        "name",
        "created_by",
    ]

    list_display = [
        "name",
        "description",
        "created_by",
    ]


class TaskAdmin(admin.ModelAdmin):

    list_filter = [
        "priority",
        "status",
        "deadline",
    ]
    list_display = [
        "title",
        "view_status",
        "view_priority",
        "assigned_to__username",
        "deadline",
    ]

    @admin.display(empty_value="???")
    def view_status(self, obj):
        return str(obj.get_status_display())

    @admin.display(empty_value="???")
    def view_priority(self, obj):
        return str(obj.get_priority_display())

    def save_model(self, request, obj, form, change):
        notify_about_task_by_email.delay(obj.id)
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
