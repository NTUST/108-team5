from django.shortcuts import render, redirect
from .models import Forum, Post, Comment, Thumb
from users.models import UserProfile
from . import forms



# Create your views here.
def index(request):
    posts = Post.objects.all()
    postsCPP = Post.objects.filter(forum__title='C++')
    postsJava = Post.objects.filter(forum__title='Java')
    postsPython = Post.objects.filter(forum__title='Python')
    postsOther = Post.objects.filter(forum__title='Other')

    query = request.GET.get('srch-term')
    if query:
        posts = Post.objects.filter(title__contains=query)
        postsCPP = Post.objects.filter(forum__title='C++').filter(title__contains=query)
        postsJava = Post.objects.filter(forum__title='Java').filter(title__contains=query)
        postsPython = Post.objects.filter(forum__title='Python').filter(title__contains=query)
        postsOther = Post.objects.filter(forum__title='Other').filter(title__contains=query)

    context = {
        'posts': posts,
        'postsCpp':postsCPP,
        'postsJava':postsJava,
        'postsPython':postsPython,
        'postsOther':postsOther
    }
    return render(request, 'forum/index.html', context)

def forum(request):
    post = Post.objects

    context = {
        'post': post
    }

    return render(request, 'forum/forum.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)
    thumb = Thumb.objects.filter(post=post)
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
        'thumb':thumb,
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
                return redirect(f'/forum/')
        else:
            form = forms.UpdateForm()

    context = {
        'form': form
    }
    return render(request, 'forum/update.html', context)