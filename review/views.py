from django.shortcuts import render, HttpResponse
from django.views import View
from review import models


# Create your views here.
def teacher(request):
    allteacher = models.Teacher.objects.all()
    return render(request, 'teacher.html', locals())


def Allclass(request):
    return HttpResponse(request.method)


def student(request):
    return HttpResponse(request.method)
