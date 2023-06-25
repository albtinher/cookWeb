from django.db import models


class CategoriaCookie(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre


class Cookie(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaCookie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    
class ConfiguracionCookie(models.Model):
    nombre = models.CharField(max_length=100)
    categoriasActivas = models.ManyToManyField(CategoriaCookie)    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    
    @property
    def categorias_activas_ids(self):
        return self.categoriasActivas.values_list('id', flat=True)
    
    def __str__(self):
        return self.nombre
    

# WEBSITES
class URL(models.Model):
    url = models.URLField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.url