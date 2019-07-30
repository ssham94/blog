from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length= 255)
    body = models.TextField()
    draft = models.BooleanField(default= False)
    published_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return f"{self.title}"