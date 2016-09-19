# -*-coding:utf-8 -*-
# 
# Created on 2016-08-21, by felix
#

from django.conf.urls import url
from .views import ContactUS

urlpatterns = [
    url(r'^$', ContactUS.as_view(), name='contact_us'),
]


