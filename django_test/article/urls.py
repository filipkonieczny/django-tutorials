from django.conf.urls import patterns, include, url

import article

urlpatterns = patterns('',
    url(r'^all/', 'article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
)