from django.contrib import admin
from .models import Forum, Post, Thumb, Comment
# Register your models here.
admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(Thumb)
admin.site.register(Comment)