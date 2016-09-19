# -*-coding:utf-8 -*-
# 
# Created on 2016-08-21, by felix
#

from django.views.generic import TemplateView


class ContactUS(TemplateView):
    """
    联系我们
    """

    template_name = 'contact.html'

    def GET(self, request, *args, **kwargs):
        return super(ContactUS, self).render_to_response({})