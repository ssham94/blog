from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import *

def home_page(request):
    context = {'articles': Article.objects.order_by('-published_date').filter(draft = False).all()}
    response = render(request, 'index.html', context)
    return response

def article(request, id):
    article = Article.objects.get(pk=id)
    context = {'article': article}
    return render(request, 'article.html', context)