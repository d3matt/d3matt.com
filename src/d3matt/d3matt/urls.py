from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd3matt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^d3matt/rv', 'd3matt.views.request_viewer'),
    url(r'^d3matt/md', 'd3matt.views.md_test'),
    url(r'^d3matt/blog/add', 'blog.views.addblog'),
    url(r'^d3matt(\/)+$', 'd3matt.views.front'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/d3matt/'}),
)
