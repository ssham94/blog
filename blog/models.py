from django.db import models
from datetime import datetime, date
from django.forms import ModelForm
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django import forms



class Article(models.Model):
    title = models.CharField(max_length= 255)
    body = models.TextField(validators = [MinLengthValidator(1)])
    draft = models.BooleanField(default= False)
    published_date = models.DateTimeField(default = datetime.now())
    user = models.ForeignKey(User, default = 1, on_delete=models.CASCADE, related_name = 'article')


    def __str__(self):
        return f"{self.title}"


class DateInput(forms.DateInput):
    input_type = 'date'

class ArticleForm(ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'body', 'draft', 'published_date']
        widgets = {
            'published_date': DateInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        draft = cleaned_data.get('draft')
        published_date = cleaned_data.get('published_date')
        today = datetime.now()
        if draft:
            if published_date <= today:
                self.add_error('published_date', 'The data must be in the future for a draft')
        else: 
            if published_date > today:
                self.add_error('published_date', 'The published date cannot be in the future')
        


class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.name}'s comment'"