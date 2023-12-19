from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html' ,
                  {"posts": posts,
                  "title": "Home"})

def about(request):
    return render(request, 'blog/about.html')

def create(request):
    form = PostForm()
    return render(request, 'blog/create.html', {'form': form})