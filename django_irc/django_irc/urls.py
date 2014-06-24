from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_irc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # admin page
    url(r'^admin/', include(admin.site.urls)),


    # main page
    url(r'^$', 'django_irc.views.homepage'),


    # register
    url(r'^register/$', 'django_irc.views.register_user'),


    # login
    url(r'^login/$', 'django_irc.views.login_user'),
    url(r'^login/auth/$', 'django_irc.views.auth_view'),
    url(r'^login/win/$', 'django_irc.views.logged_in'),
    url(r'^login/fail/$', 'django_irc.views.invalid_login'),
    url(r'^logout/$', 'django_irc.views.logout'),


    # djirc app
    url(r'^djirc/$', include('djirc.urls')),
    url(r'^djirc/create/$', 'djirc.views.create_comment')

)
