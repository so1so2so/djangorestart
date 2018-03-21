#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.forms import Form
from django.forms import widgets
from django.forms import fields
from models import Teacher
from django.db import models

class StatusCodeEnum:

    Failed = 1000
    AuthFailed = 1001
    ArgsError = 1002

    Success = 2000
    # 发帖

    # 评论

    # 点赞
    FavorPlus = 2301
    FavorMinus = 2302


class Errorform():
    def __init__(self):
        self.status = False
        self.code = StatusCodeEnum.Success
        self.data = None
        self.summary = None
        self.message = {}


class LoginForm(Form):
    user = fields.CharField(widget=widgets.TextInput(),
                            label='用户名',
                            error_messages={'required': '您输入的格式不正确，请重新输入'},
                            )
    email = fields.CharField(widget=widgets.EmailInput())
    phone = fields.IntegerField(widget=widgets.EmailInput())
    passwd = fields.CharField(widget=widgets.PasswordInput())


class TeacherForm(Form):
    Teacher_name = fields.CharField(error_messages={'required': '您输入的格式不正确，请重新输入'})
    sex = fields.IntegerField(widget=widgets.Select(choices=Teacher.choise))
    age = fields.IntegerField()


class AllclassForm(Form):
    class_name = fields.CharField(error_messages={'required': '您输入的格式不正确，请重新输入'})
    choise = Teacher.objects.all().values_list('id', 'Teacher_name')
    teacher = fields.MultipleChoiceField(choices=choise)
