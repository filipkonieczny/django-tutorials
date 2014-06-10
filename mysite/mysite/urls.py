from django.conf.urls import patterns, include, url

from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),

    # ex: / (nothing)
    # url(r'^$', views.index, name='index'),

    url(r'^', include('main_page.urls', namespace="main_page")),
)