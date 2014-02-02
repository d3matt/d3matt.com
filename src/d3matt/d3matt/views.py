import json

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


LINKS = [
    ('blog', '/d3matt/'),
    ('md test', '/d3matt/md'),
]

def request_viewer(request):
    response = HttpResponse(content_type='text/plain; charset=utf-8')
    response.write(repr(request))
    return response

def front(request, *args, **kwargs):
    return render_to_response('frontpage.html', {'LINKS': LINKS, 'PAGE': 'frontpage'}, context_instance=RequestContext(request))

def md_test(request, *args, **kwargs):
    return render_to_response('md_test.html', {'LINKS': LINKS, 'PAGE': 'md test'}, context_instance=RequestContext(request))
