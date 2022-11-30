from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from base.models import Post 
from .models import CustomUser

@login_required(login_url='login')
def profile(request: HttpRequest, username: str) -> HttpResponse:
    posts = Post.objects.filter(author__username=username)
    try:
        user = CustomUser.objects.get(username=username)
    except:
        return HttpResponse('User not found or deleted')
    context = {
        'posts': posts,
        'user': user
    }   
    return render(request, 'users/profile.html', context)

@login_required(login_url='login')
def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('home')
