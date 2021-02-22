from django.db import models

# Create your models here.
class AdminData(models.Model):
    username = models.TextField(max_length=100, unique=True)
    password = models.TextField(max_length=100)
    dept_id = models.TextField(max_length=50)
    admin = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class StudentData(models.Model):
    username = models.TextField(max_length=100, unique=True)
    password = models.TextField(max_length=100)
    dept_id = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)