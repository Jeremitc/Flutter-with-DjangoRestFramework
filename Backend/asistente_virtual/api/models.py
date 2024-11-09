from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Interaccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comando = models.TextField()
    respuesta = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
