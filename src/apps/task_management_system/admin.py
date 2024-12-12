from django.contrib import admin

from apps.task_management_system.models import Project, Task


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


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
