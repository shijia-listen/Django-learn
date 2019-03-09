from django.db import models

# Create your models here.
class Classes(models.Model):

    title=models.CharField(max_length=32)
    t=models.ManyToManyField('Teachers')

class Teachers(models.Model):

    name=models.CharField(max_length=30)

class Students(models.Model):

    name=models.CharField(max_length=32)
    age=models.IntegerField()
    gender=models.BooleanField()
    cs=models.ForeignKey(Classes,on_delete=models.CASCADE)

