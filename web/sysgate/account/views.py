from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import login as login_auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as login_view
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.views.generic import View

from .forms import LoginForm, RegistroForm
from .models import User


def login(request):
    kwargs = {
        'template_name': 'account/login.html',
        'authentication_form': LoginForm}
    return login_view(request,
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
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login_auth(request, new_user)
            messages.info(request, 'Gracias por registrarse. Sesión abierta')
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegistroForm()
    return render(request, 'account/registro.html', {'form': form})


@login_required
def profile(request):
    ctx = {'usuario': User.objects.get(id=request.user.id)}
    return TemplateResponse(request, 'account/profile.html', ctx)
