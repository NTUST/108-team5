from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/')
    level = models.IntegerField(default=0)
    aboutme = RichTextField(default='')

    def __str__(self):
        return self.user.username