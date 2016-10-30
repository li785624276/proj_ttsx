from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^redirect1/$', views.redirect1, name='redirect1'),
    # url(r'^redirect2/$', views.redirect2, name='redirect2'),
    # url(r'^cityTest/$', views.cityTest, name='cityTest'),
    # url(r'^pro/$', views.pro, name='pro'),
    # url(r'^pro(?P<id>[0-9]+)/$', views.proDetail, name='proDetail'),
    # url(r'^verifycode/$', views.verifycode, name='verifycode'),
    # url(r'^pag(?P<pIndex>[0-9]*)/$', views.pagTest, name='pagTest'),
]
