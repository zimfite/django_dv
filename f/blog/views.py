from django.shortcuts import render, redirect
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
    if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
    form = PostForm()
    return render(request, 'blog/create.html', {'form': form})