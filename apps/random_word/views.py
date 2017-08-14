# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string


# Create your views here.
def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 1
    if not 'randWord' in request.session:
        request.session['randWord'] = get_random_string(length=14)
    return render(request,'random_word/index.html')

def genRand(request):
    if request.method == "POST":
        request.session['counter'] += 1
        request.session['randWord'] = get_random_string(length=14)
        return redirect('/random_word')
    else:
        return redirect('/random_word')

def reset(request):
    request.session['counter'] = 1
    request.session['randWord'] = get_random_string(length=14)    
    return redirect('/random_word')