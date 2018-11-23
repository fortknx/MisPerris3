from django.shortcuts import render
from ApiMascotas import models
from . import serializers
from rest_framework import generics

# Create your views here.
class ListMascota(generics.ListCreateAPIView):
    queryset = models.Mascota.objects.all()
    serializer_class = serializers.MascotaSerializer


class DetalleMascota(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mascota.objects.all()
    serializer_class = serializers.MascotaSerializer