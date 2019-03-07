from django.contrib import admin
from app01 import models
#user:listen   pwd:admin123
# Register your models here.
#给某个表做个定制
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','price','pub_date')  #显示后台字段
    # ordering = ('price',)
    search_fields = ("name",'price')
    list_filter = ('name',)
    list_editable = ("price",) #可编辑的
    filter_horizontal = ("authors",)#水平筛选  必须为多对多的表
    list_per_page = 5  #显示每页的条数





admin.site.register(models.Author)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Publish)
