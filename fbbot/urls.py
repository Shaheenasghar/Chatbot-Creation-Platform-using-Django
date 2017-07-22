# FYPfinal/fbbot/urls.py
from django.conf.urls import include, url
from .views import FbBotView
urlpatterns = [
                  url(r'^2e0caeed8c6d232e12fdad32358f2fa55eae03e92ca69731f2/?$', FbBotView.as_view())
               ]