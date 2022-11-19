from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse 

@login_required(login_url='login')
def new_post(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'post/new_post.html', context)
