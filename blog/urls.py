from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.postList, name='postList'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.postDetail, name='postDetail'),
    url(r'^post/new/$', views.postNew, name='postNew'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.postEdit, name='postEdit'),
]
