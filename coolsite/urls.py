from django.conf.urls.static import static

from coolsite import settings
from women.views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound