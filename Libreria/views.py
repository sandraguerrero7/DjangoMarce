from django.shortcuts import HttpResponse, redirect, render

# Create your views here.

def saludos(request):
    return HttpResponse('Hola a todos')

def welcome(request):
    return HttpResponse('Hello everybody')


def books(request, name=None, author= None):
    if name and author:
         return HttpResponse('Book Name: ' + name + '<br> Author: ' + author)
    elif name:
        return HttpResponse('Book Name: ' + name)
    elif author:
        return HttpResponse('Author: ' + author)
    else:
        return HttpResponse('No book information provided.')


def authors(request):
    return HttpResponse('No author information provided.')

def general(request):
    return redirect('/author/')


def library(request):
    return render(request, 'books/index.html')