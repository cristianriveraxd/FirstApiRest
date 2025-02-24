import os
import django
import requests
from .models import *

def sync_data(model, url, mapping):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            obj, created = model.objects.update_or_create(
                id=item["id"], defaults={key: item[value] for key, value in mapping.items()}
            )
            
            if created:
                print(f"Nuevo registro creado para ID {item['id']}")
            else:
                print(f"Registro con ID {item['id']} actualizado.")
        
        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")


def getUsersJuan():
    sync_data(UsuariosJD, "http://54.157.69.113:8000/api/usuarios/", {
        "nombre": "nombre",
        "email": "email"
    })

def getOrderJuan():
    sync_data(PedidoJD, "http://54.157.69.113:8000/api/pedidos/", {
        "producto": "producto",
        "cantidad": "cantidad",
        "usuario": "usuario"
    })

def getUsersJorge():
    sync_data(UsuariosJorge, "http://18.221.57.79:8000/api/usuarios/", {
        "nombre_usuario": "nombre_usuario",
        "email_usuario": "email_usuario",
        "contrasena_usuario": "contrasena_usuario",
        "perfil": "perfil"
    })

def getProfileJorge():
    sync_data(PerfilJorge, "http://18.221.57.79:8000/api/Perfil/", {
        "nombre_perfil": "nombre_perfil"
    })

def getClientRocha():
    sync_data(ClienteRocha, "http://18.190.176.232:8000/api/clientes/", {
        "nombre": "nombre",
        "email": "email"
    })
