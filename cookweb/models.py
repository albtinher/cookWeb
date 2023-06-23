from django.db import models


class CategoriaCookie(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    activado = models.BooleanField(default=True)


    def __str__(self):
        return self.nombre


class Cookie(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    
class ConfiguracionCookie(models.Model):
    nombre = models.CharField(max_length=100)
    preferencias = models.ManyToManyField(Cookie)

    def __str__(self):
        return self.nombre
    

# WEBSITES
class URL(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url