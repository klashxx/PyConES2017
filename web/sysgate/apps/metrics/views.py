from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Metrica
from .serializers import SerializerMetricas


class Home(View):
    def get(self, request, *args, **kwargs):
        metricas = Metrica.objects.all().order_by('tipo')
        return render(request,
                      'metrics/home.html',
                      context={'metricas': metricas})


class MetricasViewSet(viewsets.ModelViewSet):
    serializer_class = SerializerMetricas
    http_method_names = ['get']
    filter_backends = (OrderingFilter, SearchFilter,)
    search_fields = ('tipo',)


    def get_queryset(self):
        queryset = Metrica.objects.all()
        tipo = self.request.query_params.get('tipo', None)

        if tipo is not None:
            queryset = queryset.filter(tipo=tipo)
        return queryset