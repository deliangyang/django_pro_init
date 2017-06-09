# --*- coding -*-- Created by deliang on 6/1/17.

from django.utils.deprecation import MiddlewareMixin

from django.contrib import *

from importlib import import_module
from django.conf import settings
from django.middleware.security import SecurityMiddleware

class TestMiddle(MiddlewareMixin):

    def __init__(self, get_response=None):
        MiddlewareMixin.__init__(self, get_response)
        self.get_response = get_response

    def process_request(self, request):
        print request.META.get('REMOTE_ADDR', '<none>')
        pass

    def process_template_response(self,request,response):
        print 1111111

    def process_view(self, request, view_func, view_args, view_kwargs):
        print view_args, view_kwargs


class TemplateTestMiddle(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


    def process_template_response(self, request, response):
        print 1111111
        print response.template_name
        return response

