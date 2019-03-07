from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=20,verbose_name='姓名')
    price=models.IntegerField('价格')#默认第一个参数是别名
    pub_date=models.DateField('出版日期')
    publish=models.ForeignKey("Publish",on_delete=models.CASCADE)#一对多
    authors=models.ManyToManyField("Author")  #多对多
    def __str__(self):
        return self.name

 #外键建立在多的一方
class Publish(models.Model):
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=20)


    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=20)

    def __str__(self):
        return self.name

