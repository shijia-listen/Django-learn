# _*_ encoding:utf-8 _*_
__author__ = 'listen'
__date__ = '2019/2/16 11:04'
from django import forms
from django.forms import fields
from django.forms import widgets
from django.core.validators import RegexValidator,ValidationError
from .models import *
class MyForm(forms.Form):
    username=fields.CharField(
        label='用户名：',
        required=True,
        max_length=15,
        min_length=2,
        error_messages={'required':'不能为空',
                        'max_length':'超出了最大长度',
                        'min_length':'长度太小'}
        )
    email=fields.EmailField(
        label='邮箱：',
        required=True
    )
    phone=fields.IntegerField(
        label='手机号：',
        required=True,
        validators=[RegexValidator(r'^[0-9]+$','请输入数字'),RegexValidator(r'^159[0-9]+$','数字必须为159开头')],
        error_messages={'invalid':'请正确输入'}

    )
    #验证用户名是否和数据库里面有重复  增加信息的时候使用
    #单字段验证
    # def clean_username(self):
    #     v=self.cleaned_data['username']
    #     if User_info.objects.filter(username=v).count():
    #         raise ValidationError('用户名已存在')
    #     return v
