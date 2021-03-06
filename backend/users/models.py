from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100),
    password = models.CharField(max_length=100),
    createdAt = models.DateTimeField(auto_now_add=True),
    boards = models.ForeignKey('Board', on_delete=models.CASCADE),
