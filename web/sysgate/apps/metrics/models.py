from django.db import models
from django.utils.timezone import now


class Metrica(models.Model):
    nombre = models.CharField(primary_key=True, max_length=30)
    TIPO = (
        ('c', 'Custom'),
        ('d', 'Disk'),
        ('p', 'CPU'),
        ('n', 'Network'),
    )
    tipo = models.CharField(max_length=1, choices=TIPO, default='c')
    alta = models.DateTimeField(auto_now_add=True, editable=False)
    modificacion = models.DateTimeField(default=now, blank=False)
    descripcion = models.TextField(max_length=300, blank=True)

    class Meta:
        verbose_name = 'Métrica'
        verbose_name_plural = 'Métricas'
