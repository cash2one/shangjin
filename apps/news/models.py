# -*-coding:utf-8 -*-
# 
# Created on 2016-08-12, by felix
#

from django.db import models
from utils.DjangoUeditor.models import UEditorField


class News(models.Model):
    title = models.CharField(verbose_name=u'新闻标题', max_length=50)
    content = UEditorField(verbose_name=u'正文', width=1200, height=800, imagePath='news/')
    is_published = models.BooleanField(verbose_name=u'是否发布', default=False)
    publish_time = models.DateTimeField(verbose_name=u'发布时间')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = u'新闻'

