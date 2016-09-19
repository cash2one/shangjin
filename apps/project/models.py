# -*-coding:utf-8 -*-
# 
# Created on 2016-08-15, by felix
#

from django.db import models
from utils.DjangoUeditor.models import UEditorField


class Project(models.Model):
    name = models.CharField(verbose_name=u'项目名称', max_length=20)
    city = models.CharField(verbose_name=u'城市', max_length=20)
    address = models.CharField(verbose_name=u'项目地址', max_length=50)
    phone = models.CharField(verbose_name=u'联系电话', max_length=20)
    show_img = models.ImageField(verbose_name=u'外部展示图片', help_text='240*150', upload_to='pro_show')
    content = UEditorField(verbose_name=u'正文', width=1200, height=800, imagePath='project/')
    publish_date = models.DateField(verbose_name=u'发布时间')
    is_published = models.BooleanField(verbose_name=u'是否发布', default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'项目'
        verbose_name_plural = u'项目'


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, verbose_name=u'项目')
    big_img = models.ImageField(verbose_name=u'项目大图片', help_text='691*405', upload_to='pro_big')
    small_img = models.ImageField(verbose_name=u'项目小图片', help_text='150*95', upload_to='pro_small')
    order = models.IntegerField(verbose_name=u'展示顺序', default=0)

    class Meta:
        verbose_name = u'项目图片'
        verbose_name_plural = u'项目图片'
