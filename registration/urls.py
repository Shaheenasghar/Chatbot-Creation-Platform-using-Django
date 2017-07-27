from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'registration'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^customer/add/$', views.UserFormView.as_view(), name='customer-add'),

]