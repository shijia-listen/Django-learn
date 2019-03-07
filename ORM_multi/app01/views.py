from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')
def add_book(request):
    # publish_obj=Publish.objects.filter(name='人民出版社')[0]  #拿到这条记录  对象
    # Book.objects.create(name='go', price=20, pub_date='1990-05-22', publish=publish_obj)#把publish_obj对应的id给publish
    # # Book.objects.create(name='go',price=20,pub_date='1990-05-22',publish_id=2)

    #万能的双下划线   在城市北京出版的书名字和价格
    # ret=Book.objects.filter(publish__city='北京').values('name','price')
    # print(ret)

    # #正向查找（万能的双下划线）字段名__另一个表的字段名
    # ret2=Book.objects.filter(name='python').values('publish__name')
    # # #反向查找  表名__字段名
    # ret3=Publish.objects.filter(book__name='python').values('name')
    # print(ret2)
    # print(ret3)
    #
    # #正向查找 和 反向查找（操作对象）直接是字段名
    book_obj=Book.objects.filter(name='python')[0]
    pub_obj=book_obj.authors.all()
    print(pub_obj)
    # #反向查询 表名_set
    # pub_obj1=Publish.objects.filter(name='人民出版社')[0]
    # ret5=pub_obj1.book_set.all().values('name','price')
    # print(ret5)



    return HttpResponse('添加成功！')