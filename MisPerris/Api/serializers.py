from rest_framework import serializers
from ApiMascotas import models


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'descripcionMascota',
            'nombreMascota',
        )
        model = models.Mascota
