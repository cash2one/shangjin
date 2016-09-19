# -*-coding:utf-8 -*-
# 
# Created on 2016-08-21, by felix
#

from django.conf.urls import url
from .views import AboutUS, Structure

urlpatterns = [
    url(r'^$', AboutUS.as_view(), name='about_us'),
    url(r'structure/$', Structure.as_view(), name='structure'),
]