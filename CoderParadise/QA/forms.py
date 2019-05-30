from django import forms

from ckeditor.fields import RichTextFormField
from .models import Question, QuestionType
from django.forms import widgets



class QuestionCreateForm(forms.Form):
    title = forms.CharField(help_text='Title')
    body = RichTextFormField()
    questionType = forms.ChoiceField(choices=[(choice.pk, choice.name) for choice in QuestionType.objects.all()])