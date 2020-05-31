from django.shortcuts import render,HttpResponse
from .models import Post

# Create your views here.

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts} )

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/detail.html', {'post': post})

def post_create(request):
    return HttpResponse('<b>Post Create Bebeyimm</b>')

def post_update(request):
    return HttpResponse('<b>Post Update Bebeyimm</b>')

def post_delete(request):
    return HttpResponse('<b>Post Delete Bebeyimm</b>')
