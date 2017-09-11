from django.conf.urls import url

from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
]
