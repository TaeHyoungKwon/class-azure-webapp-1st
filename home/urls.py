from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^rule/$', views.rule, name='rule'),
    url(r'^tree/$', views.tree, name='tree'),
    url(r'^signup_ok/$', TemplateView.as_view(
        template_name='registration/signup_ok.html'
    ), name='signup_ok'),

        url(r'^signup/$',views.user_new,name='user_new'),

]