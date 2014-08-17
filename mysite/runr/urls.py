from django.conf.urls import patterns, include, url

from runr import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^[a-z]{4}/$', views.new_timer, name='new_timer'),
    url(r'^(?P<key>[a-z]{4})/$', views.show_timer, name='show_timer'),
)
