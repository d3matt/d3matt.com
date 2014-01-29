from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog.forms import BlogAuthForm
from d3matt.views import LINKS
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^d3matt/rv', 'd3matt.views.request_viewer'),
    url(r'^d3matt/md', 'd3matt.views.md_test'),
    url(r'^d3matt/blog/add', 'blog.views.addblog'),
    url(r'^d3matt(\/)+$', 'd3matt.views.front'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'authentication_form': BlogAuthForm, 'extra_context': {'LINKS': LINKS}}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/d3matt/'}),
)
