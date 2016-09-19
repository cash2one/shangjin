# -*-coding:utf-8 -*-
# 
# Created on 2016-08-15, by felix
#

from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponseRedirect, Http404, JsonResponse


class PaginateMixin(object):
    """
    分页处理
    """

    allow_empty = True
    page_size = 20
    paginate_orphans = 0
    paginator_class = Paginator
    page_kwarg = 'page'

    def range_list(self, page):
        num = page.number
        total = page.paginator.num_pages
        page_range = list(page.paginator.page_range)

        if num <= 5:
            return page_range[:6]
        elif num > total - 3:
            return page_range[total-6:total]
        else:
            return page_range[num-3:num+3]

    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1

        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404("Page is not 'last', nor can it be converted to an int.")
        try:
            page = paginator.page(page_number)
            page.range_list = self.range_list(page)
            return page
        except InvalidPage as e:
            raise Http404('Invalid page (%(page_number)s): %(message)s' % {
                'page_number': page_number,
                'message': str(e)
            })

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True, **kwargs):
        """
        Return an instance of the paginator for this view.
        """
        return self.paginator_class(
            queryset, per_page, orphans=orphans,
            allow_empty_first_page=allow_empty_first_page, **kwargs)

    def get_paginate_orphans(self):
        """
        Returns the maximum number of orphans extend the last page by when
        paginating.
        """
        return self.paginate_orphans

    def get_allow_empty(self):
        """
        Returns ``True`` if the view should display empty lists, and ``False``
        if a 404 should be raised instead.
        """
        return self.allow_empty
