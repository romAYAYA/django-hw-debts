from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=300, blank=True, null=False)
    description = models.TextField(blank=True, null=False, default="")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = "django_app"
        ordering = (
            "created_at",
            "-title",
        )
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"<Task {self.title}({self.id})/ >"
