#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.shortcuts import render, HttpResponse
from django.views import View
from review import models
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from forms import LoginForm, TeacherForm, AllclassForm, Errorform
import json


# CACHE_TTL=getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)
# Create your views here
# @cache_page(10)
def teacher(request):
    if request.method == "GET":
        allteacher = models.Teacher.objects.all()[0:10]
        return render(request, 'teacher.html', {'allteacher': allteacher})
    if request.method == "POST":
        del_id = request.POST.get("t_id")
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        nid = request.POST.get("nid")
        print name, age, sex, nid
        if del_id:
            models.Teacher.objects.filter(id=del_id).delete()
        if nid:
            update_obj = models.Teacher.objects.get(id=nid)
        else:
            update_obj = models.Teacher()
        update_obj.Teacher_name = name
        update_obj.age = age
        cho = update_obj.choise
        for name in cho:
            if name[1] == sex:
                update_obj.sex = name[0]
                print "更新成功"
        update_obj.save()
        return HttpResponse("提交成功")


def Allclass(request):
    # obj =models.Allclass.objects.get(id=1)
    # obj.teacher.clear()
    # obj.save()
    # obj_revesole=models.Teacher.objects.get(id=12)
    # obj_revesole.allclass_set.add(*[1,2,3,4,5,6,7,8,9,10])
    # obj_revesole.allclass_set.add(*[1,2,3,4,10,11,15,16])
    # obj_revesole.allclass_set.clear()
    if request.method == "POST":
        name = request.POST.get("name", None)
        pwd = request.POST.get("pwd", None)
        if name == 'zhang' and pwd == '123':
            request.session['username'] = name
            return HttpResponse("登录成功")
    elif request.method == "GET":
        # request.session.set_expiry(10)
        return render(request, 'login.html', locals())


def student(request):
    allstudents = models.Students.objects.all()
    return render(request, 'students.html', locals())


def teacher_change(request):
    if request.method == "GET":
        nid = request.GET.get("nid", None)
        change = models.Teacher.objects.filter(id=nid)
    if request.method == "POST":
        nid = request.POST.get('id')
    return render(request, 'teacher_change.html', locals())


def login(request):
    if request.method == 'GET':
        obj = LoginForm()
        return render(request, 'login.html', locals())
    elif request.method == 'POST':
        obj = LoginForm(request.POST)
        obj.is_valid()
        print obj.cleaned_data
        print obj.errors.as_json
        return render(request, 'login.html', locals())


def teacher2(request):
    if request.method == 'GET':
        obj = TeacherForm()
        return render(request, 'teacher2.html', locals())
    elif request.method == 'POST':
        obj = TeacherForm(request.POST)
        obj.is_valid()
        print obj.cleaned_data
        print obj.errors.as_json
        return render(request, 'teacher2.html', locals())


def Allclass2(request):
    if request.method == 'GET':
        obj = AllclassForm()
        choist = models.Teacher.objects.all().values_list('id', 'Teacher_name')
        # print choist
        return render(request, 'allclass.html', locals())
    elif request.method == 'POST':
        ret_obj = Errorform()
        obj = AllclassForm(request.POST)
        if obj.is_valid():
            print obj.cleaned_data
            obj_is_in = models.Allclass.objects.filter(class_name=obj.cleaned_data['class_name']).count()
            if obj_is_in != 0:
                ret_obj.message['classname'] = '班级已存在'
                return HttpResponse(json.dumps(ret_obj.__dict__))
            models.Allclass.objects.create(
                class_name=obj.cleaned_data['class_name']
            ).teacher.add(*obj.cleaned_data['teacher'])
            print "返回数据正常",
        else:
            ret_obj.message['classname'] = '数据格式不正确'
            ret_obj.status = False
            print obj.errors
            print obj.errors.as_json
        return HttpResponse(json.dumps(ret_obj.__dict__))
