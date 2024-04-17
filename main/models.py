from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    contents = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.contents
