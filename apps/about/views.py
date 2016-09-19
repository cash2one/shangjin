# -*-coding:utf-8 -*-
# 
# Created on 2016-08-21, by felix
#

from django.views.generic import TemplateView

from .models import About


class AboutUS(TemplateView):
    """
    关于我们
    """

    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        about = About.objects.filter(is_published=True)
        return super(AboutUS, self).render_to_response({'about': about[0]})


class Structure(TemplateView):
    """
    组织架构
    """

    template_name = 'structure.html'

    def get(self, request, *args, **kwargs):
        return super(Structure, self).render_to_response({})