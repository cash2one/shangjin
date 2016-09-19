# -*-coding:utf-8 -*-
# 
# Created on 2016-08-08, by felix
#

from django.conf.urls import url
from .views import IndexView, Disclaimer, Privacy

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^disclaimer/$', Disclaimer.as_view(), name='disclaimer'),
    url(r'^privacy/$', Privacy.as_view(), name='privacy'),
]

