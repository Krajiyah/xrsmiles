from django.conf.urls import patterns, url

from charities import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<charity_id>[0-9]+)/$', views.show, name='show')
)