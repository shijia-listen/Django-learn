from django.shortcuts import render,redirect,HttpResponse
from .form_add import *
from .models import *
# Create your views here.
def user(request):
    user_list=User_info.objects.all()
    return render(request,'user.html',{'user_list':user_list})
def add_user(request):
    if request.method=='GET':
        obj=MyForm()
        return render(request,'add.html',{'obj':obj})
    else:
        obj=MyForm(request.POST)
        if obj.is_valid():
            User_info.objects.create(**obj.cleaned_data)
            return redirect('/user/')
        return render(request,'add.html',{'obj':obj})

def edit_user(request,nid):
    if request.method=='GET':
        m_obj=User_info.objects.filter(id=nid).first()
        obj=MyForm({'username':m_obj.username,'email':m_obj.email,'phone':m_obj.phone})
        return render(request,'edit_user.html',{'obj':obj,'nid':nid})
    else:
        obj=MyForm(request.POST) #request.POST是一个queryDict对象
        # print(request.POST)
        if obj.is_valid():
            # print(obj.cleaned_data)  clean_data是一个字典
            User_info.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/user/')
        else:
            return render(request, 'edit_user.html', {'obj': obj, 'nid': nid})



def ajax_form(request):
    if request.method=='GET':
        obj=MyForm()
        return render(request,'ajax_form.html',{'obj':obj})
    else:
        import json
        ret={'status':'fail','message':None}
        obj=MyForm(request.POST)
        if obj.is_valid():
            ret['status']='success'
            return HttpResponse(json.dumps(ret))
        ret['message']=obj.errors
        return HttpResponse(json.dumps(ret))

