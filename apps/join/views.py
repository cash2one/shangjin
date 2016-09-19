# -*-coding:utf-8 -*-
# 
# Created on 2016-08-21, by felix
#
from django.http import Http404

from django.views.generic import TemplateView

from .models import Position
from base.mixins import PaginateMixin


class TalentConcept(TemplateView):
    """
    人才理念
    """

    template_name = 'talent.html'

    def get(self, request, *args, **kwargs):
        return super(TalentConcept, self).render_to_response({})


class JoinUs(TemplateView, PaginateMixin):
    """
    人才招聘
    """

    template_name = 'join.html'
    page_size = 6

    def get(self, request, *args, **kwargs):
        position = Position.objects.filter(is_published=True).order_by('-publish_date')
        page_obj = self.paginate_queryset(position, self.page_size)

        return super(JoinUs, self).render_to_response({'page_obj': page_obj})


class JoinUsDetail(TemplateView):
    """
    招聘详情
    """

    template_name = 'join_detail.html'

    def get(self, request, *args, **kwargs):
        try:
            position = Position.objects.get(id=kwargs.get('id'), is_published=True)
        except (Position.DoesNotExist, ValueError):
            raise Http404

        return super(JoinUsDetail, self).render_to_response({'position': position})
