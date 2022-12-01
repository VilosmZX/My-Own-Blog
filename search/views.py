from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from base.models import Post
from users.models import CustomUser
from django.db.models.query import Q


def search(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        query = request.POST.get('query')
        posts = Post.objects.filter(title__icontains=query)
        users = CustomUser.objects.filter(Q(username__icontains=query)|Q(email__icontains=query))
        ctx = {
            'posts': posts,
            'users': users
        }
        return render(request, 'search/searchpage.html', ctx)
    ctx = {}
    return render(request, 'search/searchpage.html', ctx)
