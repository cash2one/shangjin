# -*-coding:utf-8 -*-
# 
# Created on 2016-08-27, by felix
#

from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'publish_time')


admin.site.register(News, NewsAdmin)
