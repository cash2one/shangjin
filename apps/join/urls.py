# -*-coding:utf-8 -*-
# 
# Created on 2016-08-21, by felix
#

from django.conf.urls import url
from .views import TalentConcept, JoinUs, JoinUsDetail

urlpatterns = [
    url(r'^talent_concept/$', TalentConcept.as_view(), name='talent_concept'),
    url(r'^us/$', JoinUs.as_view(), name='join_us'),
    url(r'^us/list/(?P<page>\d+)/$', JoinUs.as_view(), name='join_us_list'),
    url(r'^us/(?P<id>\d+)/$', JoinUsDetail.as_view(), name='join_us_detail'),
]