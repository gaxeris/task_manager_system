# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from .tasks import notify_about_task_by_email


# Project Views
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


# Task Views
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["priority", "status", "deadline"]
    search_fields = ["priority", "status", "assigned_to", "assigned_to_str"]

    def get_queryset(self):
        if self.kwargs.get("project_id"):
            return self.queryset.filter(project_id=self.kwargs.get("project_id"))
        return self.queryset.all()

    def perform_create(self, serializer):
        instance = serializer.save(created_by=self.request.user)
        task_id = instance.id
        notify_about_task_by_email.delay(task_id)


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        if self.kwargs.get("project_id"):
            return get_object_or_404(
                self.get_queryset(),
                project_id=self.kwargs.get("project_id"),
                pk=self.kwargs.get("pk"),
            )
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))

    def perform_update(self, serializer):
        instance = serializer.save()
        task_id = instance.id
        notify_about_task_by_email.delay(task_id)
