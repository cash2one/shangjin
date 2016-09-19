# -*-coding:utf-8 -*-
# 
# Created on 2016-08-27, by felix
#

from django.db import models

from utils.DjangoUeditor.models import UEditorField


class About(models.Model):
    content = UEditorField(verbose_name=u'正文', width=1200, height=800, imagePath='about/')
    is_published = models.BooleanField(verbose_name=u'是否发布', default=False)

    class Meta:
        verbose_name = u'上锦简介'
        verbose_name_plural = u'上锦简介'