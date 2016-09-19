# -*-coding:utf-8 -*-
# 
# Created on 2016-08-27, by felix
#

from django.contrib import admin

from .models import Position


class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'address', 'is_published', 'publish_date')


admin.site.register(Position, PositionAdmin)
