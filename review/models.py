#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20, verbose_name="学生姓名")
    # teacher = models.ManyToManyField("Teacher")
    allclass = models.ForeignKey("Allclass")
    age = models.IntegerField(verbose_name="年龄", default=None)
    choise = (
        (0, "男"),
        (1, "女"),
        (2, "未知"),
    )
    phone = models.IntegerField(verbose_name="电话", default=None)
    sex = models.IntegerField(verbose_name="性别", choices=choise, default=2)

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = "学生表"

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    Teacher_name = models.CharField(max_length=20, verbose_name="教师名称")
    choise = (
        (0, "男"),
        (1, "女"),
        (2, "未知"),
    )
    sex = models.IntegerField(verbose_name="性别", choices=choise, default=2)
    age = models.IntegerField(verbose_name="年龄", default=None)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = "教师表"

    def __unicode__(self):
        return self.Teacher_name


class Allclass(models.Model):
    class_name = models.CharField(max_length=20, verbose_name="班级名称")
    teacher = models.ManyToManyField("Teacher")

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = "班级表"

    def __unicode__(self):
        return self.class_name
