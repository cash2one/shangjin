# -*-coding:utf-8 -*-
# 
# Created on 2016-08-08, by felix
#

from django.db import models


class Banner(models.Model):
    banner_img = models.ImageField(verbose_name=u'首页图片', help_text='1500*500', upload_to='banner')
    title = models.CharField(verbose_name=u'标题', max_length=50)
    link = models.CharField(verbose_name=u'链接', max_length=300, blank=True, null=True)
    order = models.IntegerField(verbose_name=u'展示顺序', default=0)

    class Meta:
        verbose_name = u'首页图片'
        verbose_name_plural = u'首页图片'
