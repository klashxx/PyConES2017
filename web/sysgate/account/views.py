from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as django_login
from django.shortcuts import redirect, render

from .forms import LoginForm, RegistroForm


def login(request):
    kwargs = {
        'template_name': 'account/login.html',
        'authentication_form': LoginForm}
    return django_login(request,
                        extra_context={'site_name': settings.SITE_NAME,
                                       'title': 'Autenticación'},
                        **kwargs)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Usuario desconectado.')
    return redirect(settings.LOGIN_REDIRECT_URL)

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegistroForm()
    return render(request, 'account/registro.html', {'form': form})
