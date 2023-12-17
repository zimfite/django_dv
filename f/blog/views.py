from django.shortcuts import render
from.models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html' ,
                  {"posts": posts,
                  "title": "Home"})

def about(request):
    return render(request, 'blog/about.html')