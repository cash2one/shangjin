# -*-coding:utf-8 -*-
# 
# Created on 2016-08-27, by felix
#

from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = ('order', )


admin.site.register(Banner, BannerAdmin)
admin.site.unregister(Group)
