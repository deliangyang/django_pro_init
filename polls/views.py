# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from polls.models import Article, Reporter
import time
import json

from django.shortcuts import render

# Create your views here.

def index(request):
    reporter = Reporter()
    reporter.full_name = 'this is the reporter full name'
    reporter.save()

    articles = Article.objects.all()
    for article in articles:
        print article.reporter.full_name
       # print json.dumps(str(article.delete()))
    article = Article()
    article.pub_date = time.strftime('%Y-%m-%d')
    article.headline = 'xxxxxx'
    article.content = 'hello world'
    article.reporter_id = reporter.id
    article.save()

    return HttpResponse("hello world, Your're at the polls index.")

