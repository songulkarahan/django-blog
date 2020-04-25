from django.shortcuts import render,HttpResponse

# Create your views here.

def post_index(request):
    return HttpResponse('<b>Post İndex Bebeyimm</b>')

def post_detail(request):
    return HttpResponse('<b>Post Detail Bebeyimm</b>')

def post_create(request):
    return HttpResponse('<b>Post Create Bebeyimm</b>')

def post_update(request):
    return HttpResponse('<b>Post Update Bebeyimm</b>')

def post_delete(request):
    return HttpResponse('<b>Post Delete Bebeyimm</b>')
