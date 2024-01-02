from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post

# Create your views here.

def home(request):
    if request.method == 'POST':
        post = request.POST.get('post')
        Post.objects.create(post = post)
        return redirect(reverse('home'))
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})
