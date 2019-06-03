from django.shortcuts import render, redirect
from .models import Forum, Post, Comment, Thumb
from users.models import UserProfile
from . import forms



# Create your views here.
def index(request):
    return render(request, 'forum/index.html')

def forum(request, id):
    forumType = Forum.objects.get(pk=id)
    post = Post.objects.filter(forum=forumType)

    context = {
        'post': post
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
                body = form.cleaned_data.get('commentBody')
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

def update(request, id):
    user = request.user
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = forms.UpdateForm(request.POST)
        if form.is_valid():
            idd = form.cleaned_data.get('forum')
            forum = Forum.objects.get(pk=idd)
            post.forum = forum
            post.title = form.cleaned_data.get('title')
            post.body = form.cleaned_data.get('body')
            post.postUser=user

            post.save()
            return redirect(f'/forum/detail/{id}')
    else:
        form = forms.UpdateForm({'forum':post.forum, 'title':post.title, 'body':post.body})

    context = {
        'form': form
    }

    return render(request, 'forum/update.html', context)


def create(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = forms.UpdateForm(request.POST)
            if form.is_valid():
                idd = form.cleaned_data.get('forum')
                forum = Forum.objects.get(pk=idd)
                title = form.cleaned_data.get('title')
                body = form.cleaned_data.get('body')
                postUser=user
                post = Post(forum=forum, title=title, body=body, postUser=postUser)
                post.save()
                return redirect(f'/forum/forum/{idd}')
        else:
            form = forms.UpdateForm()

    context = {
        'form': form
    }
    return render(request, 'forum/update.html', context)