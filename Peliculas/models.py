from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=250, verbose_name="Título de la película")
    genre = models.CharField(max_length=100, verbose_name="Género de la película")
    director = models.CharField(max_length=150, verbose_name="Nombre del director")
    release_year = models.IntegerField(verbose_name="Año de publicación")
    synopsis = models.TextField(verbose_name="Sinopsis")

    def __str__(self):
        return f"{self.title} - {self.release_year}"