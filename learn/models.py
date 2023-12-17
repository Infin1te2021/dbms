# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Learn(models.Model):
    id = models.AutoField(primary_key=True)
    authorId=models.ForeignKey('login.Author',verbose_name="作者",on_delete=models.CASCADE)
    subscribeNum=models.IntegerField(verbose_name="订阅数",default=0)
    title = models.CharField(max_length=50,verbose_name=u"标题")
    content = models.TextField(verbose_name=u"内容")
    feedback = models.TextField(verbose_name=u"反馈",default="")
    status = models.CharField(max_length=50, verbose_name=u"更新状况")
    c_time = models.DateTimeField(verbose_name=u"创建时间",auto_now_add=True)
    def __str__(self):
        return str(self.title)
    class Meta:
        ordering = ['c_time']
        db_table='learn'
        verbose_name = '小说'
        verbose_name_plural = verbose_name
