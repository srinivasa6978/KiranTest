# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
   today = datetime.datetime.now().date()
   return render(request, "hello.html", {"today" : today})


def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def viewArticle(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)
def static(request):
   return render(request, 'static.html', {})
