from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    due_date = models.DateField()
    priority = models.CharField(max_length=20, default='Medium')
    status = models.BooleanField(default=False)