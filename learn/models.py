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

class supplier(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=50,verbose_name="供应名称")
    cname=models.CharField(max_length=50,verbose_name="联系人名称")
    phone_num = models.CharField(max_length=50,verbose_name=u"电话")
    email = models.CharField(max_length=50, verbose_name=u"邮箱")
    address = models.CharField(max_length=50, verbose_name=u"地址")
    #supply = models.ForeignKey('supplier',verbose_name=u"创建时间",auto_now_add=True)
    # def __str__(self):
    #     return str(self.title)
    class Meta:
        ordering = ['sid']
        db_table='supplier'
        verbose_name = '供应商'
        verbose_name_plural = verbose_name
class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50,verbose_name="名称")
    category=models.IntegerField(verbose_name="类别")
    brand = models.CharField(max_length=50,verbose_name=u"品牌")
    price = models.IntegerField(verbose_name=u"价格")
    description = models.TextField(verbose_name=u"描述",default="")
    quantity = models.IntegerField( verbose_name=u"数量")
    sid = models.ForeignKey('supplier', on_delete=models.CASCADE,null=True)
    # def __str__(self):
    #     return str(self.title)
    class Meta:
        ordering = ['id']
        db_table='goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

