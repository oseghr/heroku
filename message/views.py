from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts }
    return render(request, "message/index.html", context)


def about(request):
    context = { 'post': Post }
    return render(request, "message/about.html", context)


