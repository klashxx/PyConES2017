from django.shortcuts import render
from django.views.generic import View

from .models import Metrica


class Home(View):

    def get(self, request, *args, **kwargs):
        metricas = Metrica.objects.all().order_by('tipo')
        return render(request,
                      'metrics/home.html',
                      context={'metricas': metricas})
