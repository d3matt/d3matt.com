import json

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response

LINKS = [
    ('frontpage', '/d3matt'),
    ('md test', '/d3matt/md'),
]

def request_viewer(request):
    response = HttpResponse(content_type='text/plain; charset=utf-8')
    response.write(repr(request))
    return response

def front(request):
    return render_to_response('frontpage.html', {'LINKS': LINKS, 'PAGE': 'frontpage'})

def md_test(request):
    return render_to_response('md_test.html', {'LINKS': LINKS, 'PAGE': 'md test'})
