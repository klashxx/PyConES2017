from django.contrib import admin

from .models import Metrica


@admin.register(Metrica)
class MetricaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    list_filter = ('tipo',)
    readonly_fields=('alta', 'modificacion', )
    fields = (
        ('tipo', 'nombre',),
        ('alta',),
        'descripcion',
    )
