#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.shortcuts import render, HttpResponse
from django.views import View
from review import models
from django.utils.decorators import method_decorator


# Create your views here.
def teacher(request):
    allteacher = models.Teacher.objects.all()
    if request.method == "POST":
        del_id = request.POST.get("t_id")
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        nid= request.POST.get("nid")
        print name,age,sex,nid
        if nid:
            update_obj = models.Teacher.objects.get(id=nid)
        else:
            update_obj = models.Teacher()
            update_obj.Teacher_name = name
            update_obj.age = age
            cho = update_obj.choise
            for name in cho:
                if name[1] == sex:
                    update_obj.sex=name[0]
                    print "更新成功"
                # else:
                #     print "性别不存在，请重新选择"
            update_obj.save()
            return HttpResponse("提交成功")
        # else:
        #     models.Teacher.objects.create(
        #         Teacher_name=name,
        #         sex=2,
        #         age=age,
        #     )
        if del_id:
            models.Teacher.objects.filter(id=del_id).delete()
    return render(request, 'teacher.html', locals())


def Allclass(request):
    return HttpResponse(request.method)


def student(request):
    allstudents = models.Students.objects.all()
    return render(request, 'students.html', locals())


def teacher_change(request):
    if request.method == "GET":
        nid = request.GET.get("nid",None)
        change=models.Teacher.objects.filter(id=nid)
    if request.method == "POST":
        nid=request.POST.get('id')
    return render(request, 'teacher_change.html', locals())
