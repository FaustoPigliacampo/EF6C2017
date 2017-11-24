# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    Se modela de esta forma, para usar el atributo lista como el codigo que aparecera en el voto.
    El nombre, partido y edad, son atributos que se mostraran en una lista de candidatos.
    """
    lista = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    partido = models.CharField(max_length=30)
    edad = models.IntegerField()



class Votos(models.Model):
    """
    Cuando un usuario se presenta tiene que ingresar su numero de documento obligatoriamente,
    si el numero de documento es nulo, el usuario no voto.

    """
    nro_documento = models.IntegerField(default=0)
    lista = Candidato.objects.all()