from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    what = models.TextField()
    done = models.BooleanField()
    author = models.ForeignKey(
        User,
        related_name='tasks',
        on_delete=models.CASCADE
    )  # task_set

