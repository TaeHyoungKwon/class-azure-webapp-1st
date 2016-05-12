from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^rule/$', views.rule, name='rule'),
    url(r'^tree/$', views.tree, name='tree'),

]