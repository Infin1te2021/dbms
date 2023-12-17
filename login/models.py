# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from django.db import models
from learn.models import Learn
# Create your models here.
gender = (
    ('male', '男'),
    ('female', '女'),
)
class Reader(models.Model):
    id = models.AutoField(primary_key=True)
    readerId=models.CharField(max_length=16,verbose_name="读者账号", unique=True)
    readerName = models.CharField(max_length=15,verbose_name=u"姓名")
    password = models.CharField(max_length=16,verbose_name=u"密码")
    phone = models.CharField(max_length=11, verbose_name=u"手机号", unique=True)
    age = models.IntegerField(verbose_name="年龄",null=True)
    sex = models.CharField(verbose_name=u"性别", max_length=32, choices=gender, default='男')
    subscribe = models.ManyToManyField('learn.Learn',blank=True,verbose_name="订阅小说")
    feedback = models.TextField(verbose_name=u"反馈",null=True)
    c_time = models.DateTimeField(verbose_name=u"创建时间",auto_now_add=True)
    def __str__(self):
        return str(self.readerId)
    class Meta:
        ordering = ['c_time']
        db_table='reader'
        verbose_name = '读者'
        verbose_name_plural = verbose_name
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    authorId=models.CharField(max_length=16,verbose_name="作者账号", unique=True)
    authorName = models.CharField(max_length=5,verbose_name=u"姓名")
    password = models.CharField(max_length=16,verbose_name=u"密码")
    phone = models.CharField(max_length=11, verbose_name=u"手机号", unique=True)
    age = models.IntegerField(verbose_name="年龄",null=True)
    sex = models.CharField(verbose_name=u"性别", max_length=32, choices=gender, default='男')
    writing = models.CharField(max_length=11, verbose_name=u"写作时长",null=True)
    content = models.TextField(verbose_name=u"写作信息",null=True)
    c_time = models.DateTimeField(verbose_name=u"创建时间",auto_now_add=True)
    def __str__(self):
        return str(self.authorId)
    class Meta:
        ordering = ['c_time']
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name