from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models.query import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment, User
from .forms import PostForm

def home(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    categorys = Category.objects.all()
    context = {
        'posts': posts,
        'categorys': categorys
    }
    return render(request, 'base/home.html', context)

def category(request: HttpRequest, category: str) -> HttpResponse:
    posts = Post.objects.filter(category__name=category)
    categorys = Category.objects.all()
    context = {
        'posts': posts,
        'categorys': categorys
    }
    return render(request, 'base/home.html', context)
def post(request: HttpRequest, id: str) -> HttpResponse:
    post = Post.objects.get(id=id)
    related_posts = Post.objects.exclude(id=post.id).filter(category=post.category)
    comments = Comment.objects.filter(post=post)
    
    if request.method == 'POST':
        comment = Comment.objects.create(
            author=request.user,
            post=post,
            comment=request.POST.get('comment'),
        )
        return redirect('post', id=post.id)
    
    context = {
        'post': post,
        'related_posts': related_posts,
        'comments': comments
    }
    return render(request, 'base/room.html', context)


def login_page(request: HttpRequest) -> HttpResponse:
    
    if (request.user.is_authenticated): return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(Q(username=email) | Q(email=email))
        except:
            messages.error(request, 'User doesnt exists')
            
        user = authenticate(request, username=email, password=password)
        
        if user is None:
            user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong username or password')
        
    context = {}
    return render(request, 'base/login.html', context)

@login_required(login_url='login')
def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('home')

def register_user(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        profile_pic = request.FILES.get('profile_pic') 
        
        if password != confirm_password:
            messages.add_message(request, messages.ERROR, 'Kofirmasi password tidak valid!')
            return redirect('register')
            
        user_exists = User.objects.filter(Q(username=username) | Q(email=username)).exists()
        
        if user_exists:
            messages.add_message(request, messages.ERROR, 'User dengan sudah terdaftar!')
            
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            profile_pic=profile_pic
        )
        
        login(request, user)
        return redirect('home')
    
    ctx = {}
    return render(request, 'base/register.html', ctx)
        
        
            
    

