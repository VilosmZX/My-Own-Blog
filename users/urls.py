from django.urls import path 
from . import views 

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('admin/ban/<str:username>', views.ban_user, name='ban_user'),
    path('admin/unban/<str:username>', views.unban_user, name='unban_user')
]