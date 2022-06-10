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

