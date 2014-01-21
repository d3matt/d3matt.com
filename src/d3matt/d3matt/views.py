import json

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response

def request_viewer(request):
    response = HttpResponse(content_type='text/plain; charset=utf-8')
    response.write(repr(request))
    return response

def front(request):
    return render_to_response('frontpage.html', None)
