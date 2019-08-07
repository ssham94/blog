from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import *
from blog.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

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
    context = {"form": form, "message": "Create New Article", "action": "/article/create", "time_now": datetime.now()}
    return render(request, 'form.html', context)

def create_article(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save(commit = False)
        article.user = request.user
        article.save()
        return HttpResponseRedirect("/home")
    else:
        context = {"form": form}
        return render(request, 'form.html', context) 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username = username, password = pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                form.add_error('username', 'Login Failed')
    else:
        form = LoginForm()
    context = {'form': form}
    return HttpResponse(render(request, 'login.html', context))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return HttpResponseRedirect('/home')
    else:
        form = UserCreationForm()
    return HttpResponse(render(request, 'signup.html', {'form': form}))