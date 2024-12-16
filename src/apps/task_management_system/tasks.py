from celery import shared_task


@shared_task
def notify_about_task_by_email(task_id):
    from .models import Task

    task = Task.objects.get(id=task_id)
    task_title = task.title
    task_deadline = str(task.deadline)
    task_status = task.get_status_display()
    task_priority = task.get_priority_display()
    target = task.assigned_to
    target_name = target.username

    subject = f"Task {task_title} that has {task_priority} priority is assigned"
    message = (
        f"Greetings, {target_name}. \n\n"
        f"The task '{task_title}' status you are assigned to is set to {task_status}."
        f"Its priority is {task_priority}. Due date is {task_deadline}"
    )

    target.email_user(
        subject=subject,
        message=message,
        fail_silently=False,
    )
