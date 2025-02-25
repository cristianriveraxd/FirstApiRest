from django.db import models

class Usuarios(models.Model):
    usuario = models.CharField(max_length=80)
    contraseña = models.CharField(max_length=20)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)

    class Meta:
        db_table = 'usuarios' 

class Productos(models.Model):
    descripcion = models.CharField(max_length=80)
    stock = models.IntegerField()
    ubicacion = models.CharField(max_length=20)

    class Meta:
        db_table = 'productos'

#consumo de datos Juan David
class UsuariosJD(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'usuariosjd'

class PedidoJD(models.Model):
    usuario = models.CharField(max_length=80)
    producto = models.CharField(max_length=120)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'pedidosjd'  

#consumo de datos Jorge
class PerfilJorge(models.Model):
    nombre_perfil = models.CharField(max_length=100, unique=True) 

    class Meta:  
        db_table = 'perfiljp' 
              
class UsuariosJorge(models.Model):
    nombre_usuario = models.CharField(max_length=150)
    email_usuario = models.EmailField(unique=True)
    contrasena_usuario = models.CharField(max_length=255)
    perfil = models.CharField(max_length=100, unique=True) 

    class Meta:  
        db_table = 'usuariosjp'

#consumo de datos Leon Fael
class ClienteRocha(models.Model):
   nombre = models.CharField(max_length=100)
   email = models.EmailField(unique=True)

   class Meta:
       db_table = 'clienteslf'  

#consumo datos privados
from django.db import models

class DatosPrivados(models.Model):
    rank = models.IntegerField()  # El rango es numérico
    youtuber = models.CharField(max_length=255)
    subscribers = models.BigIntegerField()  # Los suscriptores pueden ser grandes
    video_views = models.BigIntegerField()  # Las vistas de video son grandes
    video_count = models.IntegerField()  # La cantidad de videos es numérica
    category = models.CharField(max_length=50)  # Puede necesitar más caracteres
    started = models.IntegerField()  # El año de inicio es un número entero

    class Meta:
        db_table = 'datosprivados'

    def __str__(self):
        return self.youtuber  
