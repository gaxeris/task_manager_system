from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth import get_user_model


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username"]


class TaskShortSerializer(serializers.ModelSerializer):
    priority = serializers.CharField(source="get_priority_display")
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Task
        fields = ["id", "title", "priority", "status"]


class ProjectSerializer(serializers.ModelSerializer):

    tasks = TaskShortSerializer(many=True, read_only=True)
    created_by = UserShortSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "tasks", "created_by", "created_at"]


class TaskSerializer(serializers.ModelSerializer):
    project_str = serializers.StringRelatedField(source="project.name", read_only=True)
    created_by_str = serializers.StringRelatedField(
        source="created_by.username", read_only=True
    )
    assigned_to_str = serializers.StringRelatedField(
        source="assigned_to.username", read_only=True
    )

    priority_str = serializers.CharField(source="get_priority_display", read_only=True)
    status_str = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "priority",
            "priority_str",
            "status_str",
            "status",
            "deadline",
            "project",
            "project_str",
            "assigned_to",
            "assigned_to_str",
            "created_by",
            "created_by_str",
            "created_at",
        ]
        read_only_fields = [
            "created_by",
        ]
