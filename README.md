单表操作

        表记录的添加
             
            方式一：
            Book()
            b=Book(name="python基础",price=99,author="yuan",pub_date="2017-12-12")
            b.save()
            方式二：
            Book.objects.create()
            Book.objects.create(name="老男孩linux",price=78,author="oldboy",pub_date="2016-12-12")


        表记录的修改
            方式一：
            
            b=Book.objects.get(author="oldboy")
            b.price=120
            b.save()
            
            方式二：
            #update是QuerySet
            Book.objects.filter(author="yuan").update(price=999)
         
        表记录的删除：
            Book.objects.filter(author="oldboy").delete()
            
        表记录的查询（重点）：
        
                book_list = Book.objects.filter(id=2)
                book_list=Book.objects.exclude(author="yuan").values("name","price")
                
                book_list=Book.objects.all()
                book_list = Book.objects.all()[::2]
                book_list = Book.objects.all()[::-1]
                
                #first，last,get取到的是一个实例对象，并非一个QuerySet的集合对象
                book_list = Book.objects.first()
                book_list = Book.objects.last()  
                book_list = Book.objects.get(id=2)#只能取出一条记录时才不报错
                
                
                ret1=Book.objects.filter(author="oldboy").values("name")
                ret2=Book.objects.filter(author="yuan").values_list("name","price")
                
               

                book_list= Book.objects.all().values("name").distinct()
                book_count= Book.objects.all().values("name").distinct().count()
               
            
                模糊查询  双下划线__

                book_list=Book.objects.filter(name__icontains="P").values_list("name","price")
                book_list=Book.objects.filter(id__gt=5).values_list("name","price")
                
 
      多表操作（一对多）：
               #添加记录
               #publish_id=2
               Book.objects.create(name="linux运维",price=77,pub_date="2017-12-12",publish_id=2)
               

               #publish=object
               Book.objects.create(name="GO",price=23,pub_date="2017-05-12",publish=publish_obj)
               
               #查询记录（通过对象）
               
                     正向查询：
                     book_obj=Book.objects.get(name="python")   
                     pub_obj=book_obj.publish----》书籍对象对应的出版社对象
                     pub_obj.name
                     反向查询：
                     pub_obj = Publish.objects.filter(name="人民出版社")[0]
                     pub_obj.book_set.all().values("name","price")
                     
               #查询记录（filter values  双下划线__）
                     
                    #人民出版社出版过的书籍与价格
                    ret=Book.objects.filter(publish__name="人民出版社").values("name","price")
                    
                    #python这本书出版社的名字
                    ret2=Publish.objects.filter(book__name="python").values("name")
                    
                    #python这本书出版社的名字
                    ret3=Book.objects.filter(name="python").values("publish__name")
                    
                    #北京的出版社出版书的名字
                    ret4=Book.objects.filter(publish__city="北京").values("name")
                    
                    #2017年上半年出版过书的出版社的名字
                    ret5=Book.objects.filter(pub_date__lt="2017-07-01",pub_date__gt="2017-01-01").values("publish__name")
                    
                    
     多表操作（多对多）： 
                     
                    创建多对多的关系 author= models.ManyToManyField("Author")（推荐）
                    
                    
                    书籍对象它的所有关联作者  obj=book_obj.authors.all()
                            绑定多对多的关系  obj.add(*QuerySet)   
                                              obj.remove(author_obj)
                                              
                                              
                    如果想向第三张表插入值的方式绑定关系：  手动创建第三张表

                            # class Book_Author(models.Model):
                            #     book=models.ForeignKey("Book")
                            #     author=models.ForeignKey("Author")                    
                            Book_Author.objects.create(book_id=2,author_id=3)
