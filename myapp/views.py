from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requers):
    return HttpResponse("hello,this is my app")