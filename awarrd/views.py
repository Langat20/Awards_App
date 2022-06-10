import random
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, SignupForm, UserForm, ProfileForm, RatingsForm
from .models import Post, Profile, Rating
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import User

# Create your views here.
# @login_required(login_url='login')
def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        posts = Post.objects.all()
        posts = posts[::-1]
        # a_post = random.randint(0, len(posts)-1)
        # random_post = posts[a_post]
        # print(random_post.photo)
    except Post.DoesNotExist:
        posts = None
    return render(request, 'index.html', {'posts': posts, 'form': form,})

