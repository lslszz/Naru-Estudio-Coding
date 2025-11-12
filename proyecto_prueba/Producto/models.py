from django.db import models


class Lista(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()

