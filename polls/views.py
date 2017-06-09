# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.response import  TemplateResponse
from polls.models import Article, Reporter
import time
import json

from django.shortcuts import render

# Create your views here.

def index(request):
    reporter = Reporter()
    reporter.full_name = 'this is the reporter full name'
    reporter.save()
       # print json.dumps(str(article.delete()))
    article = Article()
    article.pub_date = time.strftime('%Y-%m-%d')
    article.headline = 'xxxxxx'
    article.content = 'hello world'
    article.reporter_id = reporter.id
    article.save()

    context = {
            "title": 'hello world',
    }
    response = TemplateResponse(request, 'polls/index.html', context)

    return response


    #return HttpResponse(template.render(context))
    #return HttpResponse("hello world, Your're at the polls index.")

