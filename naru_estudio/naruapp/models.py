from django.db import models

class Usuario(models.Model):
    email = models.EmailField(
        max_length=255,
        primary_key=True,
        unique=True
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    rango = models.CharField(
        max_length=20,
        choices=[
            ('admin', 'admin'),
            ('moderador', 'moderador'),
            ('normal', 'normal'),
        ]
    )

    rol = models.CharField(
        max_length=20,
        choices=[
            ('supervisor', 'supervisor'),
            ('tutor', 'tutor'),
            ('estudiante', 'estudiante'),
        ]
    )

    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"
