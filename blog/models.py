from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length= 255)
    body = models.TextField()
    draft = models.BooleanField(default= False)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.name}'s comment'"