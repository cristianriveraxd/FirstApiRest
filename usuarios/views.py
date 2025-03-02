import requests
from rest_framework import generics, viewsets
from .models import Usuarios, Productos, UsuariosJD, PedidoJD, PerfilJorge, UsuariosJorge, ClienteRocha, DatosPrivados
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView 

#VIEWSMYAPPI
class UsuariosListCreate(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class ProductosListCreate(generics.ListCreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class ProductosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    
#VIEWSAPIJUANDA
class UsuariosJDListCreate(generics.ListCreateAPIView):
    queryset = UsuariosJD.objects.all()
    serializer_class = UsuariosJDSerializer

class UsuariosJDDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuariosJD.objects.all()
    serializer_class = UsuariosJDSerializer

class PedidoJDListCreate(generics.ListCreateAPIView):
    queryset = PedidoJD.objects.all()
    serializer_class = PedidoJDSerializer

class PedidoJDDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PedidoJD.objects.all()
    serializer_class = PedidoJDSerializer

#VIEWSAPIJORGE
class PerfilJorgeListCreate(generics.ListCreateAPIView):
    queryset = PerfilJorge.objects.all()
    serializer_class = PerfilJorgeSerializer

class PerfilJorgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerfilJorge.objects.all()
    serializer_class = PerfilJorgeSerializer   

class UsuariosJorgeListCreate(generics.ListCreateAPIView):
    queryset = UsuariosJorge.objects.all()
    serializer_class = UsuariosJorgeSerializer

class UsuariosJorgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuariosJorge.objects.all()
    serializer_class = UsuariosJorgeSerializer

#VIEWSAPIROCHA
class ClienteRochaListCreate(generics.ListCreateAPIView):
    queryset = ClienteRocha.objects.all()
    serializer_class = ClienteRochaSerializer

class ClienteRochaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ClienteRochaSerializer 


#CONSUMO DE APIS
class ApiJuanda(APIView):
    def get(self, request):
        url = "http://54.157.69.113:8000/api"  
        response = requests.get(url)
        
        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener la API de JuanDavid"}, status=500)

class ApiJorge(APIView):
    def get(self, request):
        url = "http://18.221.57.79:8000/api"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener la API de Jorge"}, status=500)

class ApiRocha(APIView):
    def get(self, request):
        url = "http://18.190.176.232:8000/api"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener la API de Rocha"}, status=500)

#CONSUMO DATOS DEL CSV
class DatosPrivadosViewSet(viewsets.ModelViewSet):
    queryset = DatosPrivados.objects.all()
    serializer_class = DatosPrivadosSerializer

#CONSUMO DE DATOS PROYECTO
class DatosPrivadosCorreoViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = DatosPrivadosCorreoSerializer

class EnvioViewSet(viewsets.ModelViewSet):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer
