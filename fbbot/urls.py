# FYPfinal/fbbot/urls.py
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from . import views
from .views import webhook

urlpatterns = [
               url(r'^webhook/(?P<partner_id>\d+)/$', views.webhook, name='webhook'),
               url(r'^newbot/$', login_required(views.BotCreate.as_view()), name='createbot'),
               url(r'^bots/$', login_required(views.BotListView.as_view()), name='listbot'),
        # url('^bots/(?P<username>.+)$', views.BotList.as_view()),
]
