from django.db import models
from django.conf import settings
STATUS_CHOICES = (
    ('PR', 'Privada'),
    ('PB', 'Publica')
)
# Create your models here.

class Lista(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(default='mi lista', max_length=50)
    STATUS_CHOICES = (
        ('PR', 'Privada'),
        ('PB', 'Publica')
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PR')

    def __str__(self):
        return self.nombre

class ListaItem(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    crusado = models.BooleanField(default=False)
    # cantidad = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.nombre
