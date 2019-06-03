from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.core.files.images import get_image_dimensions
from ckeditor.fields import RichTextFormField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileEditForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    aboutme = RichTextFormField(required=False, external_plugin_resources=[(
                                          'youtube',
                                          '/static/base/vendor/ckeditor_plugins/youtube/youtube/',
                                          'plugin.js',
                                          )])
    class Meta:
        model = User
        fields = ['email']