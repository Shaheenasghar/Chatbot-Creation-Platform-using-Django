# FYPfinal/fbbot/urls.py
from django.conf.urls import include, url

from . import views
from .views import webhook


urlpatterns = [
        url(r'^webhook$', views.webhook, name='webhook'),
        url(r'^newbot/$', views.BotCreate.as_view(), name='createbot'),
        #url('^bots/(?P<username>.+)$', views.BotList.as_view()),
]

