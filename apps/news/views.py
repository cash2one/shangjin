# -*-coding:utf-8 -*-
# 
# Created on 2016-08-12, by felix
#
from django.http import Http404

from django.views.generic import TemplateView

from .models import News
from base.mixins import PaginateMixin


class NewsList(PaginateMixin, TemplateView):
    """
    新闻列表
    """

    template_name = 'news_list.html'
    page_size = 5

    def get(self, request, *args, **kwargs):
        news = News.objects.filter(is_published=True).order_by('-publish_time')
        page_obj = self.paginate_queryset(news, self.page_size)

        return super(NewsList, self).render_to_response({'page_obj': page_obj})


class NewsDetail(TemplateView):
    """
    新闻详情
    """

    template_name = 'news_detail.html'

    def get(self, request, *args, **kwargs):
        try:
            news = News.objects.get(id=kwargs.get('id'), is_published=True)
        except (News.DoesNotExist, ValueError):
            raise Http404
        news_list = News.objects.filter(is_published=True)
        next_news = news_list.filter(publish_time__gt=news.publish_time).order_by('publish_time')[:1]
        before_news = news_list.filter(publish_time__lt=news.publish_time).order_by('-publish_time')[:1]
        return super(NewsDetail, self).render_to_response({'news': news,
                                                           'next_news': next_news[0] if next_news else '',
                                                           'before_news': before_news[0] if before_news else ''})
