from django.conf.urls import url, include

from . import views

app_name = 'metrics'

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
]
