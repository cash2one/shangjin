# -*-coding:utf-8 -*-
# 
# Created on 2016-08-27, by felix
#

from django.contrib import admin

from .models import Project, ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'is_published')


class AdminMixin(object):

    def show_name(self, obj):
        return obj.project.name
    show_name.short_description = u'名称'


class ProjectImageAdmin(admin.ModelAdmin, AdminMixin):
    list_display = ('show_name', 'order', )


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
