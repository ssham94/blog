from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import *

def home_page(request):
    context = {'articles': Article.objects.order_by('-published_date').filter(draft = False).all()}
    response = render(request, 'index.html', context)
    return response

