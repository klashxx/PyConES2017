from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='reset'),
    url(r'^password_reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    url(r'^password_change/$',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    url(r'^password_change/done/$',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registro/$', views.registro, name='registro'),
]
