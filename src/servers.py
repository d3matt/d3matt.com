#!/usr/bin/python

#IMPORTS
import sys
import os
import inspect

from twisted.application import internet, service
from twisted.web import server, static, resource
from twisted.web.wsgi import WSGIResource
from twisted.python.threadpool import ThreadPool
from twisted.internet import reactor

PROJ_ROOT = os.path.dirname(os.path.realpath(__file__))

class Root(resource.Resource):
    def __init__(self, wsgi_resource):
        resource.Resource.__init__(self)
        self.wsgi_resource = wsgi_resource

    def getChild(self, path, request):
        path0 = request.prepath.pop(0)
        request.postpath.insert(0, path0)
        return self.wsgi_resource

application = service.Application('d3matt')

# Environment setup for your Django project files:
sys.path.append("d3matt")
os.environ['DJANGO_SETTINGS_MODULE'] = 'd3matt.settings'
#os.environ['PROJ_ROOT'] = PROJ_ROOT
from django.core.handlers.wsgi import WSGIHandler

wsgiThreadPool = ThreadPool()
wsgiThreadPool.start()

reactor.addSystemEventTrigger('after', 'shutdown', wsgiThreadPool.stop)
djangoResource = WSGIResource(reactor, wsgiThreadPool, WSGIHandler())
root = Root(djangoResource)
root.putChild('static', static.File(os.path.abspath(os.path.join(PROJ_ROOT, '..', 'www', 'static'))))

web = internet.TCPServer(0, server.Site(root))
web.setServiceParent(application)
