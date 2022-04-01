from django.db import models

class PersonModel(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=100)
    provincia=models.CharField(max_length=100)
    com_aut=models.CharField(max_length=100)
    dni=models.CharField(max_length=100)
    asignatura=models.CharField(max_length=100)
    codigo_asig=models.IntegerField()
    nota=models.IntegerField()

    class Meta:
        db_table='person'