from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    profile_pic = models.ImageField(upload_to=f'user-profile/user-{str(email)}', blank=True, default='default/default.jpg')
    banned = models.BooleanField(default=False)

    def __str__(self):
        return self.email 

