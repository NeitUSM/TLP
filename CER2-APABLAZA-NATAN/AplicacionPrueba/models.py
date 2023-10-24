from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='AplicacionPrueba/static/AplicacionPrueba/img/')
    administracion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"

class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    detalle = models.TextField()
    detalle_corto = models.CharField(max_length=255)
    TIPO_CHOICES = [
        ("S", "Suspensión de Actividades"),
        ("C", "Suspensión de Clases"),
        ("I", "Información"),
    ]
    tipo = models.CharField(max_length=25, choices=TIPO_CHOICES)
    entidad = models.ForeignKey(Entidad, on_delete=models.SET_NULL, null=True, blank=True)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    publicado_por = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='publicados'
    )
    modificado_por = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='modificados'
    )

    def __str__(self):
        return self.titulo
