from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class QuestionType(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=225)
    body = RichTextField()
    questionType = models.ForeignKey(QuestionType,on_delete=models.CASCADE)
    postedUser = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    body = models.TextField()
    abouQuestion = models.ForeignKey(Question,on_delete=models.CASCADE,default=None)
    postedUser = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.body