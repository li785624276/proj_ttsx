from django.shortcuts import render
from django.http import *
from models import *
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    print('hello')
    return render(request, 'demo/index.html')
