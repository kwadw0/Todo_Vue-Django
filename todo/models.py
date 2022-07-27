from django.db import models


class Todo(models.Model):
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post
# Create your models here.
