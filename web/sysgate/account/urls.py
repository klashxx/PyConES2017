from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='account'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^password_reset/$', auth_views.password_reset, name='reset'),
    url(r'^password_reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    url(r'^password_change/$',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    url(r'^password_change/done/$',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
]
