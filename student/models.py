from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
