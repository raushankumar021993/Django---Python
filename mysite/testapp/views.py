from django.shortcuts import render
from djnago.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<H2> Hey this is Raushan Kumar </H2>")