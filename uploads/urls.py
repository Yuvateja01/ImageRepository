from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.post,name="post"),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    path('delete/all',views.deleteall,name='deleteall'),
]