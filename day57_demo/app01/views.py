from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

content_list=[]
for i in range(1,500):
    temp={'name':'xiaozhu'+str(i),'age':i}
    content_list.append(temp)

#内置分页
def in_basepage(request):
    current_page=request.GET.get('p')
    paginator=Paginator(content_list,10)  #把所有数据内容加载出来
    try:
        posts=paginator.page(current_page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    return render(request,'inbasepage.html',{"posts":posts})


#自定义分页
def basepage(request):
    from app01.pager import Pagination
    current_page=request.GET.get('p')
    page_obj=Pagination(500,current_page)
    data_list=content_list[page_obj.start():page_obj.end()]

    return render(request,'basepage.html',{'data_list':data_list,"page_obj":page_obj})
