import requests

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Metrica
from .serializers import SerializerMetricas


@method_decorator(login_required, name='dispatch')
class Home(View):
    def get(self, request, *args, **kwargs):
        r = requests.get('http://sysgate:8000/metrics/api/v1/metricas/')
        return render(request,
                      'metrics/home.html',
                      context={'metricas': r.json()})


class MetricasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SerializerMetricas
    http_method_names = ['get']
    filter_backends = (OrderingFilter, SearchFilter,)
    search_fields = ('tipo',)

    def get_queryset(self):
        queryset = Metrica.objects.all().order_by('tipo')
        tipo = self.request.query_params.get('tipo', None)

        if tipo is not None:
            queryset = queryset.filter(tipo=tipo)

        return queryset
