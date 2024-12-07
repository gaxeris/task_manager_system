from django.urls import path
from .views import (
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Project URLs
    path("projects/", ProjectListCreateView.as_view(), name="project_list_create"),
    path(
        "projects/<int:pk>/",
        ProjectRetrieveUpdateDestroyView.as_view(),
        name="project_detail_update_delete",
    ),
    # Task URLs
    path("tasks/", TaskListCreateView.as_view(), name="task_list_create"),
    path(
        "tasks/<int:pk>/",
        TaskRetrieveUpdateDestroyView.as_view(),
        name="task_detail_update_delete",
    ),
]
