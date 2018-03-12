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
        if name and age and sex:
            update_obj=models.Teacher
            update_obj.Teacher_name=name
            d = update_obj.choise=age
            print d
            # models.Teacher.objects.create(
            #     Teacher_name=name,
            #     sex=2,
            #     age=age,
            # )
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

    return render(request, 'teacher_change.html', locals())
