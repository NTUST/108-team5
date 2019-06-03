from django.shortcuts import render, redirect
from .models import Forum, Post, Comment, Thumb
from users.models import UserProfile
from . import forms

# Create your views here.
def index(request):
    return render(request, 'forum/index.html')

def forum(request, id):
    forumType = Forum.objects.get(id=id)
    post = Post.objects.filter(forum=forumType)
    thumb = Thumb.objects.filter(post=post)
    thumbCount = thumb.objects.count()

    context = {
        'post': post,
        'thumbCount':thumbCount
    }

    return render(request, 'forum/forum.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)
    thumb = Thumb.objects.filter(post=post)
    thumbCount = Thumb.objects.count()
    comment = Comment.objects.filter(post=post)
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = forms.CommentForm(request.POST)
            if form.is_valid():
                body = form.cleaned_data.get('body')
                comment = Comment(post=post, body=body, postUser=user)
                comment.save()
                return redirect(f'/forum/detail/{id}')
        else:
            form = forms.CommentForm()
    else:    
        form = forms.CommentForm()

    context = {
        'post': post,
        'thumbCount':thumbCount,
        'comments':comment,
        'commentForm':form
    }

    return render(request, 'forum/detail.html', context)


def create(request):
    return render(request, 'forum/create.html')