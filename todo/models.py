from turtle import title
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
