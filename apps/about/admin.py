# -*-coding:utf-8 -*-
# 
# Created on 2016-08-27, by felix
#

from django.contrib import admin

from .models import About


class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.register(About, AboutAdmin)
