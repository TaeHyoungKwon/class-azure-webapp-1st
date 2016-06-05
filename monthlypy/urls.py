from django.conf.urls import include, url
from . import views



urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),


    url(r'^(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),
    ]

