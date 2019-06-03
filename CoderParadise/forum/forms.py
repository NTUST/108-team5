from django import forms

from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField

from django.forms import widgets
from .models import Comment

class CommentForm(forms.Form):
    commentBody = forms.CharField()
        
    