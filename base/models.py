from django.db import models
from uuid import uuid4
from users.models import CustomUser as User

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, blank=False, null=False)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 
    
class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, blank=False, null=False)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    message = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message[:50]

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, blank=False, null=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(blank=False, null=False)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self):
        return self.title 
    
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-createdAt']
    
    def __str__(self):
        return self.comment[:50]
