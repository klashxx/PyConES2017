from rest_framework import serializers

from .models import Metrica


class SerializerMetricas(serializers.ModelSerializer):
    class Meta:
        model = Metrica
        fields = '__all__'
