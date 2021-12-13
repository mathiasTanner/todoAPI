from django.db import models

# Create your models here.

class List (models.Model):
    ListId = models.AutoField(primary_key=True)
    ListName = models.CharField(max_length=500)

class Task (models.Model):
    TaskId = models.AutoField(primary_key=True)
    TaskName = models.CharField(max_length=500)
    List = models.IntegerField()
    Deadline = models.DateField()
    Status = models.BooleanField(null=True)