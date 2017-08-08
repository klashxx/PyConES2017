"""
SYSGATE URL Configuration
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^account/', include('account.urls'), name='Autenticación'),
    url(r'^admin/', admin.site.urls),
]
