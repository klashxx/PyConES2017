from django.conf.urls import url, include
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^password_reset/$', auth_views.password_reset),
    url(r'^password_reset/done/$', auth_views.password_reset_done),
    url(r'^', include('django.contrib.auth.urls')),
]
