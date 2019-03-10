from django.db import models

# Create your models here.
class User_info(models.Model):
    username=models.CharField(max_length=15)
    email=models.EmailField()
    phone=models.IntegerField()
