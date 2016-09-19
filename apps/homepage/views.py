# -*-coding:utf-8 -*-
# 
# Created on 2016-08-08, by felix
#

from django.views.generic import TemplateView

from .models import Banner
from apps.news.models import News
from apps.project.models import Project


class IndexView(TemplateView):
    """
    首页
    """

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        banner = Banner.objects.all().order_by('-order')
        news = News.objects.filter(is_published=True).order_by('-publish_time')[:5]
        project = Project.objects.filter(is_published=True).order_by('-publish_date')

        return super(IndexView, self).render_to_response({'banner': banner, 'news': news, 'project': project})


class Disclaimer(TemplateView):
    """
    免责声明
    """

    template_name = 'disclaimer.html'


class Privacy(TemplateView):
    """
    隐私条款
    """

    template_name = 'privacy.html'
