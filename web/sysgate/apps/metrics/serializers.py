from rest_framework import serializers

from .models import Metrica


class SerializerMetricas(serializers.ModelSerializer):

    long_tipo = serializers.SerializerMethodField()

    def get_long_tipo(self, obj):

        if obj.tipo == 'n':
            return 'Network'
        elif obj.tipo == 'd':
            return 'Disk'
        elif obj.tipo == 'p':
            return 'CPU'
        return 'Custom'

    class Meta:
        model = Metrica
        fields = '__all__'
