from django.shortcuts import redirect,render,HttpResponse
from .models import *

def get_classes(request):
    classes_list=Classes.objects.all()
    # for i in classes_list:
    #     print(i.id,i.title,i.t.all())

    # print(teachers_list)



    return render(request,"get_classes.html",{"classes_list":classes_list,


    })

def get_teachers(request):
    if request.method == 'GET':
        uid=request.GET.get('uid')
        cls_obj=Classes.objects.filter(id=uid).first()
        ids=cls_obj.t.all().values_list('id','name')
        id_list=list(list(zip(*ids))[0]) if list(zip(*ids)) else []
        # print(id_list)
        teachers_list=Teachers.objects.all()
        return render(request,'get_teachers.html',{"teachers_list":teachers_list,
                                                        'id_list':id_list,
                                                   'uid':uid,})
    elif request.method == 'POST':
        uid=request.GET.get('uid')
        tea_id=request.POST.getlist('tea_id')
        obj=Classes.objects.filter(id=uid).first()
        obj.t.set(tea_id)   #根据value


        return redirect('/get_classes')



def add_classes(request):
    if request.method == 'GET':
        return render(request, 'add_classes.html')
    elif request.method == 'POST':
        title=request.POST.get('title')
        Classes.objects.create(title=title)
        return redirect('/get_classes')

def update_classes(request):
    if request.method == 'GET':
        uid=request.GET.get('uid')
        obj=Classes.objects.filter(id=uid).first()
        return render(request, 'update_classes.html',{'obj':obj})
    elif request.method == 'POST':
        id=request.GET.get('uid')
        title=request.POST.get('title')
        Classes.objects.filter(id=id).update(title=title)
        return redirect('/get_classes')

def del_classes(request):
    id=request.GET.get('uid')
    Classes.objects.filter(id=id).delete()
    return redirect('/get_classes')



def get_students(request):
    students_list=Students.objects.all()

    return render(request,'get_students.html',{"students_list":students_list})


def add_students(request):
    if request.method == 'GET':
        classes_list=Classes.objects.all()
        return render(request,'add_students.html',{'classes_list':classes_list})
    elif request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        cs=request.POST.get('cs')
        Students.objects.create(name=name,age=age,gender=gender,cs_id=cs)
        return redirect('/get_students')

def update_students(request):
    if request.method == 'GET':
        classes_list = Classes.objects.all()
        uid=request.GET.get('uid')
        obj=Students.objects.filter(id=uid).first()
        return render(request,'update_students.html',{"obj":obj,"classes_list":classes_list})
    elif request.method == 'POST':
        uid=request.GET.get('uid')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cs = request.POST.get('cs')
        Students.objects.filter(id=uid).update(name=name,age=age,gender=gender,cs_id=cs)
        return redirect('/get_students')

def del_students(request):
    uid=request.GET.get('uid')
    Students.objects.filter(id=uid).delete()
    return redirect('/get_students')


def teacher_index(request):
    teacher_list=Teachers.objects.all()
    return render(request,'teacher_index.html',{
        'teacher_list':teacher_list
    })

def add_teachers(request):
    if request.method == 'GET':

        return render(request,'add_teachers.html')
    elif request.method == 'POST':
        name=request.POST.get('name')
        Teachers.objects.create(name=name)
        return redirect('/teacher_index')

def update_teachers(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        obj=Teachers.objects.filter(id=uid).first()
        return render(request,'update_teachers.html',{'obj':obj})
    elif request.method == 'POST':
        uid=request.GET.get('uid')
        name=request.POST.get('name')
        Teachers.objects.filter(id=uid).update(name=name)
        return redirect('/teacher_index')


def del_teacher(request):
    uid=request.GET.get('uid')
    Teachers.objects.filter(id=uid).delete()
    return redirect('/teacher_index')

def give_classes(request):
    if request.method == 'GET':
        uid=request.GET.get('uid')
        class_list=Classes.objects.all()
        tea_obj=Teachers.objects.filter(id=uid).first()
        ids=tea_obj.classes_set.all().values_list('id','title')
        # print(ids)
        # id_list=list(zip(*ids))
        id_list = list(list(zip(*ids))[0]) if list(zip(*ids)) else [] #zip能把qurry对象变为分组--还是对象 list变为一个列表  取第一个元素变为元组，之后变为列表

        # print(id_list)

        return render(request,'give_classes.html',{'class_list':class_list,
                                                         'id_list':id_list,
                                                        'uid':uid,
    })
    elif request.method == 'POST':
        uid=request.GET.get('uid')
        cla_id=request.POST.getlist('cla_id')
        # print(cla_id)
        obj=Teachers.objects.filter(id=uid).first()
        obj.classes_set.set(cla_id)

        return redirect('/teacher_index')

def remove_ajax(request):
    nid=request.GET.get('nid')
    msg='成功'
    try:
        Students.objects.filter(id=nid).delete()
    except Exception as e:
        # msg = str(e)
     return HttpResponse(msg)














    #


