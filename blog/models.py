from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # here we have that posts can have different categories, and that categories can have different posts
    categories = models.ManyToManyField('Category', related_name='posts')
    
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # here we have one post have several comments
    post = models.ForeignKey('Post', on_delete=models.CASCADE)