#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from review import models
from django.utils.decorators import method_decorator
from django.forms import Form
from django.forms import widgets
from django.forms import fields


# Create your views here.
def teacher(request):
    allteacher = models.Teacher.objects.all()
    if request.method == "POST":
        del_id = request.POST.get("t_id")
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        if name and age and sex:
            update_obj = models.Teacher
            update_obj.Teacher_name = name
            d = update_obj.choise = age
            print d
            # models.Teacher.objects.create(
            #     Teacher_name=name,
            #     sex=2,
            #     age=age,
            # )
        if del_id:
            models.Teacher.objects.filter(id=del_id).delete()
            return HttpResponse("maa")
    return render(request, 'teacher.html', locals())


class MyForm(Form):
    class_name = fields.CharField(min_length=10,
                                  label="班级名",
                                  initial='张能',
                                  show_hidden_initial=True,
                                  error_messages={'required': '用户名不能为空',},
                                  disabled=True,
                                  label_suffix='>>>')
    # teacher = fields.IntegerField(widget=widgets.Select(choices=[(1,'张能'),(2,'未万亮'),]),
    #                            error_messages={'required': '老师不能为空'},)


def Allclass(request):
    if request.method == "GET":
        obj = MyForm()
        return render(request, 'class.html',{'obj': obj})
    elif request.method == "POST":
        obj = MyForm(request.POST)
        r1 = obj.is_valid()
        print r1
        if r1:
            print obj.clean()
            print obj.cleaned_data
        else:
            # print obj.errors['class_name'],type(obj.errors['class_name'])
            print obj.errors
            # print obj.errors['class_name'][0],type(obj.errors['class_name'][0])
        return render(request, 'class.html', {'obj': obj})


def student(request):
    allstudents = models.Students.objects.all()
    return render(request, 'students.html', locals())


def teacher_change(request):
    if request.method == "GET":
        nid = request.GET.get("nid", None)
        change = models.Teacher.objects.filter(id=nid)

    return render(request, 'teacher_change.html', locals())
