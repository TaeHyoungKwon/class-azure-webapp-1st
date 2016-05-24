"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
        
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^notice/', include('notice.urls', namespace='notice')),
    url(r'^freeboard/', include('freeboard.urls', namespace='freeboard')),
    url(r'^bamboo/', include('bamboo.urls', namespace='bamboo')),
    url(r'^meeting/', include('meeting.urls', namespace='meeting')),
    url(r'^money/', include('money.urls', namespace='money')),
    url(r'^mainpage/', include('mainpage.urls', namespace='mainpage')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^$' , lambda r: redirect('home:home')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

