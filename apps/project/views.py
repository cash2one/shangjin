# -*-coding:utf-8 -*-
# 
# Created on 2016-08-15, by felix
#
from django.http import Http404

from django.views.generic import TemplateView

from .models import Project, ProjectImage
from base.mixins import PaginateMixin


class ProjectList(TemplateView, PaginateMixin):
    """
    项目列表
    """

    template_name = 'project_list.html'
    page_size = 6

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(is_published=True)
        page_obj = self.paginate_queryset(projects, self.page_size)

        return super(ProjectList, self).render_to_response({'page_obj': page_obj})


class ProjectDetail(TemplateView):
    """
    项目详情
    """

    template_name = 'project_detail.html'

    def get(self, request, *args, **kwargs):
        try:
            project = Project.objects.get(id=kwargs.get('id'), is_published=True)
        except (Project.DoesNotExist, ValueError):
            raise Http404
        pro_imgs = project.projectimage_set.all().order_by('-order')
        first_img = pro_imgs[0] if pro_imgs else ''
        return super(ProjectDetail, self).render_to_response({'project': project, 'pro_imgs': pro_imgs,
                                                              'first_img': first_img})
