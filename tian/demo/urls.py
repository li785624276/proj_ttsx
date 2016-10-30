from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^list/$', views.list, name='list'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^loginHandle/$', views.loginHandle, name='loginHandle'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_center_info/$', views.user_center_info, name='user_center_info'),
    url(r'^user_center_site/$', views.user_center_site, name='user_center_site'),
    url(r'^user_center_order/$', views.user_center_order, name='user_center_order'),
    url(r'^place_order/$', views.place_order, name='place_order'),
]
