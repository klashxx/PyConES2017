from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'metricas', views.MetricasViewSet, 'metricas')

app_name = 'metrics'

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^api/v1/', include(router.urls)),
]
