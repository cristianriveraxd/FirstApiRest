import requests
from rest_framework import generics
from .models import Usuarios, Productos
from .serializers import UsuariosSerializer, ProductosSerializer
from rest_framework.response import Response
from rest_framework.views import APIView 

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
    
class ApiJorge(APIView):
    def get(self, request):
        url = "http://54.157.69.113:8000/api"  # API externa de ejemplo
        response = requests.get(url)
        
        if response.status_code == 200:
            return Response(response.json())  # Devolver los datos de la API externa
        else:
            return Response({"error": "No se pudo obtener datos"}, status=response.status_code)