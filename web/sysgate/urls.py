"""
SYSGATE URL Configuration
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


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
