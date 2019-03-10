from django.shortcuts import render,HttpResponse
from app01.models import *
from django.core import serializers
import json
# Create your views here.
def serelize(request):

    return render(request,'serelize.html')

def ajax_serelize(request):
    response={'status':True,'data':None}
    #方法一：
    # user_list = User_info.objects.all()
    # return render(request, 'ajax_serelize.html', {'user_list': user_list})
    #方法二
    #querry_set 类型
    # try:
    #     user_list = User_info.objects.all()  #querry_set对象  不是基本的数据类型
    #     response['data']=serializers.serialize('json',user_list)#成为基本的字符串类型
    #
    # except Exception as e :
    #     response['status']=False
    # return HttpResponse(json.dumps(response))

    #字典
    try:
        user_list = User_info.objects.all().values('username','email')  # 字典
        response['data'] = list(user_list) # 内部本来就是基本的数据类型

    except Exception as e:
        response['status'] = False
    return HttpResponse(json.dumps(response))




