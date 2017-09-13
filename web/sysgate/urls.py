"""
SYSGATE URL Configuration
"""
from django.conf import settings
from django.conf.urls import (handler400, handler403, handler404, handler500,
                              include, url)
from django.contrib import admin
from sysgate.apps.core.views import error_400, error_403, error_404, error_500

handler400 = error_400
handler403 = error_403
handler404 = error_404
handler500 = error_500

urlpatterns = [
    url(r'^', include('apps.core.urls', namespace='core')),
    url(r'^account/', include('account.urls'), name='Autenticación'),
    url(r'^metrics/', include('apps.metrics.urls'), name='Métricas'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
    urlpatterns += staticfiles_urlpatterns()
