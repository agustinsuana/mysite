from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo, esta es el index de Polls.")

def edit(request):
    return HttpResponse("Hola mundo, esta es el edit de Polls.")

def delete(request):
    return HttpResponse("Hola mundo, esta es el delete de Polls.")
