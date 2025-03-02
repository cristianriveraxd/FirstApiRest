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
    id = models.AutoField(primary_key=True)
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


class Trip(models.Model):
    id_envio = models.AutoField(primary_key=True)  
    gps_provider = models.CharField(max_length=50, blank=True, null=True)
    booking_id = models.CharField(max_length=50, blank=True, null=True)
    market_regular = models.CharField(max_length=20, blank=True, null=True)
    booking_id_date = models.DateTimeField(blank=True, null=True)
    vehicle_no = models.CharField(max_length=20, blank=True, null=True)
    origin_location = models.CharField(max_length=255, blank=True, null=True)
    destination_location = models.CharField(max_length=255, blank=True, null=True)
    org_lat_lon = models.CharField(max_length=50, blank=True, null=True)
    des_lat_lon = models.CharField(max_length=50, blank=True, null=True)
    data_ping_time = models.DateTimeField(blank=True, null=True)
    planned_eta = models.DateTimeField(blank=True, null=True)
    current_location = models.CharField(max_length=255, blank=True, null=True)
    destination_location_actual = models.CharField(max_length=255, blank=True, null=True)
    actual_eta = models.DateTimeField(blank=True, null=True)
    curr_lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    curr_lon = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ontime = models.BooleanField(default=False)
    delay = models.CharField(max_length=20, null=True, blank=True)
    origin_location_code = models.CharField(max_length=50, blank=True, null=True)
    destination_location_code = models.CharField(max_length=50, blank=True, null=True)
    trip_start_date = models.DateTimeField(blank=True, null=True)
    trip_end_date = models.DateTimeField(blank=True, null=True)
    transportation_distance_in_km = models.IntegerField(blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    minimum_kms_to_be_covered_in_a_day = models.CharField(max_length=50, blank=True, null=True)
    driver_name = models.CharField(max_length=100, blank=True, null=True)
    driver_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    customer_id = models.CharField(max_length=50, blank=True, null=True)
    customer_name_code = models.CharField(max_length=255, blank=True, null=True)
    supplier_id = models.CharField(max_length=50, blank=True, null=True)
    supplier_name_code = models.CharField(max_length=255, blank=True, null=True)
    material_shipped = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'trip_data'  

    def _str_(self):
        return f"Trip {self.id_envio} from {self.origin_location} to {self.destination_location}"
 

class Envio(models.Model):
    id = models.AutoField(primary_key=True)
    periodo = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    rango_peso_envio = models.CharField(max_length=50)
    ambito = models.CharField(max_length=50)
    tipo_envio = models.CharField(max_length=50)
    tipo_servicio = models.CharField(max_length=50)
    ingresos = models.CharField(max_length=150)
    numero_total_envios = models.IntegerField()
    
    class Meta:
        db_table = 'envios' 

    def __str__(self):
        return f"Envio {self.id} - {self.proveedor}"
