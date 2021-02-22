from django.db import models

# Create your models here.
class AdminData(models.Model):
    username = models.TextField(max_length=100, unique=True, blank=False)
    password = models.TextField(max_length=100, blank=False)
    dept_id = models.TextField(max_length=50, blank=False)
    admin = models.BooleanField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class StudentData(models.Model):
    username = models.TextField(max_length=100, unique=True, blank=False)
    password = models.TextField(max_length=100, blank=False)
    dept_id = models.TextField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)