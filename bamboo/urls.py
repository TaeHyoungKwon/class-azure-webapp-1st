from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views



urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),
	
	
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='edit_post'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),




    url(r'^(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='edit_comment'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', views.comment_delete, name='delete_comment'),
]




