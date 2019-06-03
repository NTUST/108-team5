from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Post(models.Model):
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=50)
    body = RichTextField()
    postTime = models.DateTimeField(default = datetime.now)
    postUser = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Thumb(models.Model):
    post = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

class Comment(models.Model):
    post = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    CommentTime = models.DateTimeField(default = datetime.now)
    
    def __str__(self):
        return self.post.title