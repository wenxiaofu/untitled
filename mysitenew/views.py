from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse


def index(request):
    return render(request, 'mysitenew/home.html')

# def add(request):
#     a = request.get['a'] #这种方式已经淘汰了
#     b = request.get['b']
#     c = int(a) + int(b)
#     return HttpResponse(str(c))