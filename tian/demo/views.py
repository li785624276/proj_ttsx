from django.shortcuts import render
from django.http import *
from models import *
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    dic = {
        'key1': '<b>123</b>',
        'key2': '<h1>456</h1>'
    }
    return render(request, 'booktest/index.html', dic)
