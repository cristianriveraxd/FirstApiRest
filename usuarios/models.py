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

class UsuariosJD(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'usuariosjd'

class PedidoJD(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    producto = models.CharField(max_length=120)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'pedidosjd'  