from django.shortcuts import render

# Create your views here.
from .models import Question, QuestionType, Answer

def index(request):
    datasAll = Question.objects.all()
    datasCPP = Question.objects.filter(questionType__name='C++')
    datasJava = Question.objects.filter(questionType__name='Java')
    datasPython = Question.objects.filter(questionType__name='Python')
    datasOther = Question.objects.filter(questionType__name='Other')
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
    anss = Answer.objects.filter(abouQuestion__id=id)
    context = {
        'title': 'QA',
        'data': data,
        'anss': anss,
    }
    return render(request, 'QA/detail.html', context)

def create(request):
    return render(request, 'QA/create.html')

