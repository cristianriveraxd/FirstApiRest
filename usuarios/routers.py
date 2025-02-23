from usuarios.models import *
from rest_framework import viewsets
from rest_framework import serializers
from .getData import *

#serializers MyApi
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

#serializer Api Juan David
class UsuariosJDSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosJD
        fields = '__all__'

class PedidoJDSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoJD
        fields = '__all__'

class UsuariosJDViewSet(viewsets.ModelViewSet):
    queryset = UsuariosJD.objects.all()
    serializer_class = UsuariosJDSerializer
    def get_queryset(self):
        getUsersJuan()  # 🔹 Llama a la función antes de obtener los datos
        return UsuariosJD.objects.all()

class PedidoJDViewSet(viewsets.ModelViewSet):
    queryset = PedidoJD.objects.all()
    serializer_class = PedidoJDSerializer
    def get_queryset(self):
        getOrderJuan()  # 🔹 Llama a la función antes de obtener los datos
        return PedidoJD.objects.all()
        
#serializer Api Jorge
class PerfilJorgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilJorge
        fields = '__all__'

class PerfilJorgeViewSet(viewsets.ModelViewSet):
    queryset = PerfilJorge.objects.all()
    serializer_class = PerfilJorgeSerializer
    def get_queryset(self):
        getProfileJorge()  # 🔹 Llama a la función antes de obtener los datos
        return PerfilJorge.objects.all()
    
class UsuariosJorgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosJorge
        fields = '__all__'

class UsuariosJorgeViewSet(viewsets.ModelViewSet):
    queryset = UsuariosJorge.objects.all()
    serializer_class = UsuariosJorgeSerializer
    def get_queryset(self):
        getUsersJorge()  # 🔹 Llama a la función antes de obtener los datos
        return UsuariosJorge.objects.all()
    

#serializers Api Rocha
class ClienteRochaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteRocha
        fields = '__all__'

class ClienteRochaViewSet(viewsets.ModelViewSet):
    queryset = ClienteRocha.objects.all()  # 🔹 Agrega esta línea
    serializer_class = ClienteRochaSerializer
    def get_queryset(self):
        getClientRocha()  # 🔹 Llama a la función antes de obtener los datos
        return ClienteRocha.objects.all()


