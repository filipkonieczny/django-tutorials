from django.conf.urls import patterns, url

from main_page import views

urlpatterns = patterns('',
    # ex: /main_page/
    url(r'^$', views.index, name='index'),

    # ex: /wtf/
    # r'^(?P<poll_id>\d+)/vote/$
    url(r'^wtf/', views.wtf, name='wtf'),


    # ex: /yauza
    url(r'^yauza/', views.yauza, name='yauza'),
)