# -*-coding:utf-8 -*-
# 
# Created on 2016-08-15, by felix
#

from django.conf.urls import url
from .views import ProjectList, ProjectDetail

urlpatterns = [
    url(r'^$', ProjectList.as_view(), name='project_list'),
    url(r'^list/(?P<page>\d+)/$', ProjectList.as_view(), name="project_list_page"),
    url(r'^(?P<id>\d+)/$', ProjectDetail.as_view(), name='project_detail'),
]
