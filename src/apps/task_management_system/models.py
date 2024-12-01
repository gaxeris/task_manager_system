from django.db import models
from django.conf import settings


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="projects"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("L", "Low"),
        ("M", "Medium"),
        ("H", "High"),
    ]

    STATUS_CHOICES = [
        ("P", "Pending"),
        ("IP", "In Progress"),
        ("C", "Completed"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="M")
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="P")
    deadline = models.DateField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assigned_tasks",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_tasks"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
