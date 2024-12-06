from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth import get_user_model


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username"]


class TaskShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "priority", "status"]


class ProjectSerializer(serializers.ModelSerializer):

    tasks = TaskShortSerializer(many=True, read_only=True)
    created_by = UserShortSerializer()

    class Meta:
        model = Project
        fields = ["id", "name", "description", "tasks", "created_by", "created_at"]


class ProjectShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    # project_name = serializers.StringRelatedField(source="project.name", read_only=True)
    project = ProjectShortSerializer()
    created_by = UserShortSerializer(read_only=True)
    assigned_to = UserShortSerializer()

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "priority",
            "status",
            "deadline",
            "project",
            #  "project_name",
            "assigned_to",
            "created_by",
            "created_at",
        ]
        # extra_kwargs = {"creeated_by": {"read_only": True}}
