from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'basic_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    # /
    url(r'^$', 'blog.views.index'),

    # /blog/view/slug
    url(r'^blog/view/(?P<slug>[^\.]+).html', 'blog.views.view_post', name='view_blog_post'),

    # /blog/category/slug
    url(r'^blog/category/(?P<slug>[^\.]+).html', 'blog.views.view_category', name='view_blog_category'),
)
