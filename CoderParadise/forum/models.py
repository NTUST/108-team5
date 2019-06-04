from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User
from users.models import UserProfile


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
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    thumbUser = models.ForeignKey(User,on_delete=models.CASCADE, default=None, blank=True)

    def __str__(self):
        return self.post.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    commentTime = models.DateTimeField(default = datetime.now)
    postUser = models.ForeignKey(User,on_delete=models.CASCADE, default=None, blank=True)
    
    def __str__(self):
        return self.post.title