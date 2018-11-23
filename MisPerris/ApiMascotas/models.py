from django.db import models

# Create your models here.
class Mascota(models.Model):
    title=models.CharField(max_length=30)
    codigoMascota = models.AutoField(primary_key = True)
    imagen = models.ImageField(upload_to = './media/imagenes/')
    nombreMascota = models.CharField(max_length = 30)
    razaMascota = models.CharField(max_length = 50)
    descripcionMascota = models.TextField(null = True, blank = True)
    estadoMascota = models.CharField(max_length = 50, default = "rescatado")
    def __str__(self):
        return self.title