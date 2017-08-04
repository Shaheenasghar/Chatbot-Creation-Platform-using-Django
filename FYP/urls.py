from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fb_messenger/', include('fbbot.urls')),
    url(r'', include('registration.urls'), name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
