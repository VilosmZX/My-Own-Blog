from django.urls import path 
from . import views 

urlpatterns = [
    path('post/new', views.new_post, name='new_post')
]