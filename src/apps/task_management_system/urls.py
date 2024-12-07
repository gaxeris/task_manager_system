from django.urls import path
from .views import (
    ProjectListCreateAPIView,
    ProjectDetailAPIView,
    TaskListCreateAPIView,
    TaskDetailAPIView,
)

urlpatterns = [
    # Project URLs
    path("projects/", ProjectListCreateAPIView.as_view(), name="project-list"),
    path(
        "projects/<int:pk>/",
        ProjectDetailAPIView.as_view(),
        name="project-detail",
    ),
    # Nested Task URLs
    path(
        "projects/<int:project_id>/tasks/",
        TaskListCreateAPIView.as_view(),
        name="task-list",
    ),
    path(
        "projects/<int:project_id>/tasks/<int:pk>/",
        TaskDetailAPIView.as_view(),
        name="task-detail",
    ),
]
