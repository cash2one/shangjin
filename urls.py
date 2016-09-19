# -*-coding:utf-8 -*-
#
# Created on 2016-08-08, by felix
#

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^management/backend/sj/', include(admin.site.urls)),
    url(r'^', include('apps.homepage.urls')),
    url(r'^news/', include('apps.news.urls')),
    url(r'^join/', include('apps.join.urls')),
    url(r'^about/', include('apps.about.urls')),
    url(r'^contact/', include('apps.contact.urls')),
    url(r'^project/', include('apps.project.urls')),
    url(r'^ueditor/', include('utils.DjangoUeditor.urls')),
]

admin.site.site_header = u'上锦资产 后台管理系统'
admin.site.site_title = u'上锦资产'
admin.site.index_title = u'上锦资产'

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
