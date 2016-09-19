# -*-coding:utf-8 -*-
# 
# Created on 2016-08-12, by felix
#

from django.conf.urls import url
from .views import NewsList, NewsDetail

urlpatterns = [
    url(r'^$', NewsList.as_view(), name='news_list'),
    url(r'^list/(?P<page>\d+)/$', NewsList.as_view(), name="news_list_page"),
    url(r'^(?P<id>\d+)/$', NewsDetail.as_view(), name='news_detail'),
]
