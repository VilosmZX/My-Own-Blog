from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
from django.contrib.auth.decorators import login_required
from base.models import Post 
from .models import CustomUser

@login_required(login_url='login')
def profile(request: HttpRequest, username=None) -> HttpResponse:
    posts = Post.objects.filter(author__id=request.user.id)
    context = {
        'posts': posts
    }
    
    if (username is not None): 
        posts = Post.objects.filter(author__username=username)
        try:
            user = CustomUser.objects.get(username=username)
        except:
            return HttpResponse('User not found or deleted')
        context = {
            'posts': posts
        }
    return render(request, 'users/profile.html', context)
