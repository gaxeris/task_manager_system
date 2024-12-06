from django.urls import path
from .views import (
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Project URLs
    path("projects/", ProjectListCreateView.as_view(), name="project-list"),
    path(
        "projects/<int:pk>/",
        ProjectRetrieveUpdateDestroyView.as_view(),
        name="project-detail",
    ),
    # Nested Task URLs
    path(
        "projects/<int:project_id>/tasks/",
        TaskListCreateView.as_view(),
        name="task-list",
    ),
    path(
        "projects/<int:project_id>/tasks/<int:pk>/",
        TaskRetrieveUpdateDestroyView.as_view(),
        name="task-detail",
    ),
]
