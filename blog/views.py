from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import *

def root(request):
    return HttpResponseRedirect('/home')

def home_page(request):
    context = {'articles': Article.objects.order_by('-published_date').filter(draft = False).all()}
    response = render(request, 'index.html', context)
    return response

def find_article(request, id):
    article = Article.objects.get(pk=id)
    context = {'article': article}
    return render(request, 'article.html', context)

def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.filter(id=article_id)[0]
    name = request.POST['username']
    comment = request.POST['comment']
    new_comment = Comment(name=name, message=comment, article = article)
    new_comment.save()
    context = {'article': article}
    return render(request, 'article.html', context)

def new_article(request):
    form = ArticleForm()
    context = {"form": form, "message": "Create New Article", "action": "/article/create"}
    return render(request, 'form.html', context)

def create_article(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/home")
    else:
        context = {"form": form}
        return render(request, 'form.html', context) 