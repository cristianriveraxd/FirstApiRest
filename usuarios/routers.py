from usuarios.models import *
from rest_framework import viewsets
from rest_framework import serializers

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
        model = Usuario
        fields = '__all__'

class PedidoJDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class UsuariosJDViewSet(viewsets.ModelViewSet):
    queryset = UsuariosJD.objects.all()
    serializer_class = UsuariosJDSerializer

class PedidoJDViewSet(viewsets.ModelViewSet):
    queryset = PedidoJD.objects.all()
    serializer_class = PedidoJDSerializer

#serializer Api Jorge
class PerfilJorgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilJorge
        fields = '__all__'

class PerfilJorgeViewSet(viewsets.ModelViewSet):
    queryset = PerfilJorge.objects.all()
    serializer_class = PerfilJorgeSerializer
    
    
class UsuariosJorgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosJorge
        fields = '__all__'

class UsuariosJorgeViewSet(viewsets.ModelViewSet):
    queryset = UsuariosJorge.objects.all()
    serializer_class = UsuariosJorgeSerializer
    

#serializers Api Rocha
class ClienteRochaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteRocha
        fields = '__all__'

class ClienteRochaViewSet(viewsets.ModelViewSet):
    queryset = ClienteRocha.objects.all()
    serializer_class = ClienteRochaSerializer
