from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$',views.getuser,name='user'),
    url(r'^(?P<user_id>[0-9]+)/name/$',views.getname,name='name'),
    url(r'^zip/$', views.getfiles, name='createzip')
]
