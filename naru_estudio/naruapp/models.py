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
        ],
        default='normal'
    )

    rol = models.CharField(
        max_length=20,
        choices=[
            ('supervisor', 'supervisor'),
            ('tutor', 'tutor'),
            ('estudiante', 'estudiante'),
        ],
        default='estudiante',
    )

    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"


class Entrada(models.Model):
    titulo = models.CharField(max_length=50)
    # Cascade: Si el autor desaparece, se borran sus entradas
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    resumen = models.TextField(max_length=250)
    contenido = models.TextField()

    categoria = models.CharField(
        choices=[
            ('estudio', 'estudio'),
            ('fisica', 'fisica'),
            ('matematicas', 'matematicas'),
            ('ingles', 'ingles')
        ]
    )