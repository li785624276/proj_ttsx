from django.shortcuts import render
from django.http import *
from models import *
from django.core.paginator import Paginator
from . import der
# Create your views here.


def index(request):
    print('hello')
    return render(request, 'demo/index.html')


@der.login_yz
def cart(reqeust):
    return render(request, 'demo/cart.html')


def detail(request):
    return render(request, 'demo/detail.html')


def list(request):
    return render(request, 'demo/list.html')


def login(request):
    return render(request, 'demo/login.html')


def loginHandle(request):
    uname = request.POST['uname']
    # upwd = request.POST['upwd']
    yzm = request.POST['yzm']
    if yzm.upper() == request.session['verifycode']:
        request.session['uname'] = uname
        return redirect('/')
    else:
        return redirect('/login/')


def logout(request):
    del request.session['uname']
    return redirect('/')


def register(request):
    return render(request, 'demo/register.html')


def user_center_info(request):
    return render(request, 'demo/user_center_info.html')


def user_center_site(request):
    return render(request, 'demo/user_center_site.html')


def user_center_order(request):
    return render(request, 'demo/user_center_order.html')


def cart(request):
    return render(request, 'demo/cart.html')


def place_order(request):
    return render(request, 'demo/place_order.html')
