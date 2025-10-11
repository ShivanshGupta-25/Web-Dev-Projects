from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts':posts})


def post(request,mypost):
    posts = Post.objects.get(id=mypost)
    return render(request, 'post.html',{'posts':posts})

def writeBlog(request):
    return render(request, 'writeBlog.html')