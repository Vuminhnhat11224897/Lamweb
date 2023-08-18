from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index123(request):
    return HttpResponse('HELLO dcm')