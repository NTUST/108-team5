from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', default=None, blank=True)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username