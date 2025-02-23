import os
import django
import requests
from .models import *

def getUsersJuan():
    urls = "http://54.157.69.113:8000/api/usuarios/" 
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = UsuariosJD.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                UsuariosJD.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    nombre=item["nombre"],
                    email=item["email"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")

def getOrderJuan():
    urls = "http://54.157.69.113:8000/api/pedidos/"  
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = PedidoJD.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                PedidoJD.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    producto=item["producto"],
                    cantidad=item["cantidad"],
                    usuario=item["usuario"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")

        
def getUsersJorge():
    urls = "http://18.221.57.79:8000/api/usuarios/"  
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = UsuariosJorge.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                UsuariosJorge.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    nombre_usuario =item["nombre_usuario"],
                    email_usuario =item["email_usuario"],
                    contrasena_usuario =item["contrasena_usuario"],
                    perfil =item["perfil"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")

def getProfileJorge():
    urls = "http://18.221.57.79:8000/api/Perfil/"  
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = PerfilJorge.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                PerfilJorge.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    nombre_perfil =item["nombre_perfil"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")

def getClientRocha():
    urls = "http://18.190.176.232:8000/api/clientes/"  
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = ClienteRocha.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                ClienteRocha.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    nombre =item["nombre"],
                    email =item["email"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")
        
        


    


        
        



