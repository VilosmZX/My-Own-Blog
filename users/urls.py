from django.urls import path 
from . import views 

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('delete-account/', views.delete_account, name='delete_account')
]