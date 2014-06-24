from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_irc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # djirc page(/djirc/)
    url(r'^$', 'djirc.views.djirc'),
    url(r'^/create/$', 'djirc.views.create_comment'),


)
