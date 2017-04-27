from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse

def add(request):
 #   return HttpResponse("dddddddd")
    a = request.GET.get('a', '1')
    b = request.GET.get('b', '2')
    c = int(a) + int(b)
    return HttpResponse(str(c))
def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))