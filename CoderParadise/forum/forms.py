from django import forms

from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField

from django.forms import widgets
from .models import Comment, Post, Forum

class CommentForm(forms.Form):
    commentBody = forms.CharField()

class UpdateForm(forms.Form):
    forum = forms.ChoiceField(choices=[(choice.pk, choice.title) for choice in Forum.objects.all()])
    title = forms.CharField(help_text='標題', max_length=50)
    body = RichTextFormField()

        
    