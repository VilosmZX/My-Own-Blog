from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category>/', views.category, name='category'),
    path('post/<str:id>', views.post, name='post'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]