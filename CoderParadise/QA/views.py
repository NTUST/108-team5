from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from . import forms
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
from .models import Question, QuestionType, Answer
def index(request):
    datasAll = Question.objects.all()
    datasCPP = Question.objects.filter(questionType__name='C++')
    datasJava = Question.objects.filter(questionType__name='Java')
    datasPython = Question.objects.filter(questionType__name='Python')
    datasOther = Question.objects.filter(questionType__name='Other')

    query = request.GET.get('srch-term')
    if query:
        datasAll = Question.objects.filter(title__contains=query)
        datasCPP = Question.objects.filter(questionType__name='C++').filter(title__contains=query)
        datasJava = Question.objects.filter(questionType__name='Java').filter(title__contains=query)
        datasPython = Question.objects.filter(questionType__name='Python').filter(title__contains=query)
        datasOther = Question.objects.filter(questionType__name='Other').filter(title__contains=query)
    context = {
        'title': 'QA',
        'datasAll': datasAll,
        'datasCPP': datasCPP,
        'datasJava': datasJava,
        'datasPython': datasPython,
        'datasOther': datasOther
    }
    return render(request, 'QA/index.html', context)

def findMyOA(request, username):
    user = User.objects.get(username=username)
    datasAll = Question.objects.filter(postedUser=user)
    datasCPP = Question.objects.filter(questionType__name='C++', postedUser=user)
    datasJava = Question.objects.filter(questionType__name='Java', postedUser=user)
    datasPython = Question.objects.filter(questionType__name='Python', postedUser=user)
    datasOther = Question.objects.filter(questionType__name='Other', postedUser=user)

    query = request.GET.get('srch-term')
    if query:
        datasAll = Question.objects.filter(title__contains=query).filter(postedUser=user)
        datasCPP = Question.objects.filter(questionType__name='C++').filter(title__contains=query).filter(postedUser=user)
        datasJava = Question.objects.filter(questionType__name='Java').filter(title__contains=query).filter(postedUser=user)
        datasPython = Question.objects.filter(questionType__name='Python').filter(title__contains=query).filter(postedUser=user)
        datasOther = Question.objects.filter(questionType__name='Other').filter(title__contains=query).filter(postedUser=user)

    context = {
        'title': 'QA',
        'datasAll': datasAll,
        'datasCPP': datasCPP,
        'datasJava': datasJava,
        'datasPython': datasPython,
        'datasOther': datasOther
    }
    return render(request, 'QA/index.html', context)

def detail(request, id):
    data = Question.objects.get(id=id)
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = forms.AnswerForm(request.POST)
            if form.is_valid():
                body = form.cleaned_data.get('body')
                ans = Answer( body=body, abouQuestion=data, postedUser=user)
                ans.save()
                return redirect(f'/QA/detail/{id}#footer')
        else:
            form = forms.AnswerForm()
    else:
        form = forms.AnswerForm()
    anss = Answer.objects.filter(abouQuestion__id=id)
    context = {
        'form': form,
        'title': 'QA',
        'data': data,
        'anss': anss,
    }
    return render(request, 'QA/detail.html', context)

def create(request):
    if request.user.is_authenticated:
        username = request.user.username
        if request.method == 'POST':
            form = forms.QuestionCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                body = form.cleaned_data.get('body')
                questionTypeID = form.cleaned_data.get('questionType')
                questionType = QuestionType.objects.get(id=int(questionTypeID))
                postedUser = User.objects.get(username=username)
                
                question = Question.objects.create(
                    title=title,
                    body=body,
                    questionType=questionType,
                    postedUser=postedUser
                )
                Question.save(question)
                messages.success(request, f'您以創建問題成功!')
                return redirect('/QA/')
        else:
            form = forms.QuestionCreateForm()
        return render(request, 'QA/create.html', {'form':form})
    else:
        messages.info(request, f'請您登入後再新增問題！')
        return redirect('/QA/')

