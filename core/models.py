from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=500, null = True, blank = True )
    completed = models.BooleanField(default = False)
    addedBy = models.ForeignKey(User ,on_delete=models.CASCADE, related_name = "tasks")

    def __str__(self):
        return self.title
    