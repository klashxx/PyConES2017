from django import forms
from django.contrib.auth import forms as django_forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class LoginForm(django_forms.AuthenticationForm):
    username = forms.CharField(
        label='Usuario', max_length=20)

    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request=request, *args, **kwargs)
        if request:
            username = request.GET.get('username')
            if username:
                self.fields['username'].initial = username


class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Debe ser valído')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
