from celery import shared_task
from django.core.mail import send_mail

from apps.task_management_system.models import Task


@shared_task
def notify_about_task_by_email(task_id):
    task = Task.objects.get(id=task_id)
    task_title = task.title
    task_deadline = str(task.deadline)

    target = task.assigned_to
    target_name = target.username

    subject = f"Task {task_title} is assigned"
    message = f"Greetings, {target_name}. \n\nYou are assigned to '{task_title}'. Due date is {task_deadline}"

    target.email_user(
        subject=subject,
        message=message,
        fail_silently=False,
    )
