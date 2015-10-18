from django.shortcuts import render
from django.http import HttpResponse
from src.models import Post
# Create your views here.

def index(request):
    objects = Post.objects.all()
    return render(request, 'inde.html',{'objects' : objects})

