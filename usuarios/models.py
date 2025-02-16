from django.db import models

class Usuarios(models.Model):
 
    usuario = models.CharField(max_length=80)
    contraseña = models.CharField(max_length=20)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)

    class Meta:
        db_table = 'USUARIOS' 

class Productos(models.Model):
   
    descripcion = models.CharField(max_length=80)
    stock = models.IntegerField()
    ubicacion = models.CharField(max_length=20)

    class Meta:
        db_table = 'PRODUCTOS'
