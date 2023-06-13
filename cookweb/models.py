from django.db import models

class Cookies(models.Model):
    CATEGORIA_CHOICES = [
        ('tipo1', 'Tipo 1'),
        ('tipo2', 'Tipo 2'),
        ('tipo3', 'Tipo 3'),
        ('tipo4', 'Tipo 4'),
        ('tipo5', 'Tipo 5'),
    ]
    
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)
    activado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.categoria
