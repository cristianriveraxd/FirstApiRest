from rest_framework import serializers
from .models import Usuarios, Productos, UsuariosJD, PedidoJD, PerfilJorge, UsuariosJorge, ClienteRocha, DatosPrivados, Trip, Envio

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '_all_'

class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuarios
        fields = '_all_'

class UsuariosJDSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsuariosJD
        fields = '_all_'

class PedidoJDSerializer(serializers.ModelSerializer):

    class Meta:
        model = PedidoJD
        fields = '_all_'

class PerfilJorgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerfilJorge
        fields = '_all_'

class UsuariosJorgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsuariosJorge
        fields = '_all_'

class ClienteRochaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClienteRocha
        fields = '_all_'

class DatosPrivadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosPrivados
        fields = ['youtuber']  

class DatosPrivadosCorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        
class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = '__all__'
