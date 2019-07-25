from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from random import randint
from datetime import datetime

def home_page(request):
    context = {'current_time': datetime.now()}
    response = render(request, 'index.html', context)
    return response