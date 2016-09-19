# -*-coding:utf-8 -*-
# 
# Created on 2016-08-27, by felix
#

from django.db import models
from utils.DjangoUeditor.models import UEditorField


class Position(models.Model):
    title = models.CharField(verbose_name=u'职位名称', max_length=20)
    amount = models.IntegerField(verbose_name=u'人数', default=1)
    address = models.CharField(verbose_name=u'工作地点', max_length=20)
    content = UEditorField(verbose_name=u'正文', width=1200, height=800, imagePath='news/')
    is_published = models.BooleanField(verbose_name=u'是否发布', default=False)
    publish_date = models.DateField(verbose_name=u'发布时间')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'招聘信息'
        verbose_name_plural = u'招聘信息'