from django.db import models
from datetime import datetime
from django.forms import ModelForm
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User



class Article(models.Model):
    title = models.CharField(max_length= 255)
    body = models.TextField(validators = [MinLengthValidator(1)])
    draft = models.BooleanField(default= False)
    published_date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, default = 1, on_delete=models.CASCADE, related_name = 'article')


    def __str__(self):
        return f"{self.title}"


    # def clean_dfaft(self):
    #     if draft == True:
    #         published_date > datetime.now()
    #     elif draft == False:
    #         published_date < datetime.now()

class ArticleForm(ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'body', 'draft', 'published_date']

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.name}'s comment'"