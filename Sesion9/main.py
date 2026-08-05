
import requests
def informacion_colombia():
    url = "https://api-colombia.com/api/v1/Country/Colombia"
    response = requests.get(url)
   
    if response.status_code == 200:
        data = response.json()
        print("--- INFORMACIÓN GENERAL DE COLOMBIA ---")
        print(f"Nombre: {data.get('name')}")
        print(f"Descripción: {data.get('description')}")
        print(f"Código de Moneda: {data.get('currencyCode')}")
    else:
        print("Error al conectar con la API:", response.status_code)

#informacion_colombia()

def obtener_departamentos():
    url = "https://api-colombia.com/api/v1/Department"
    response = requests.get(url)
   
    if response.status_code == 200:
        data = response.json()
        print("--- DEPARTAMENTOS DE COLOMBIA ---")
        for department in data:
            print(f"Nombre del departamento: {department.get('name')}")
            print(f"Descripción: {department.get('description')}")
            print(f"Nombre de la Capital: {department.get('cityCapital', {}).get('name')}")
            print(f"Descripción de la Capital: {department.get('cityCapital', {}).get('description')}")
            
    else:
        print("Error al conectar con la API:", response.status_code)
#obtener_departamentos()

def obtener_regiones():
    url = "https://api-colombia.com/api/v1/Region"
    response = requests.get(url)
   
    if response.status_code == 200:
        data = response.json()
        print("--- REGIONES DE COLOMBIA ---")
        for region in data:
            print(f"Nombre de la región: {region.get('name')}")
            print(f"Descripción: {region.get('description')}")
    else:
        print("Error al conectar con la API:", response.status_code)

#obtener_regiones()

def obtener_atracciones():
    url = "https://api-colombia.com/api/v1/TouristicAttraction"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("--- ATRACCIONES TURÍSTICAS DE COLOMBIA ---")
        for attraction in data:
            print(f"Nombre: {attraction.get('name')}")
            print(f"Descripción: {attraction.get('description')}")
            print(f"Ubicación: {attraction.get('city', {}).get('name')}")
    else:
        print("Error al conectar con la API:", response.status_code)

#obtener_atracciones()

def obtener_informacion(string):
    if string == "colombia":
        informacion_colombia()
    elif string == "departamentos":
        obtener_departamentos()
    elif string == "regiones":
        obtener_regiones()
    elif string == "atracciones":
        obtener_atracciones()
    else :
        print("Opción no válida. Por favor, ingrese 'colombia', 'departamentos', 'regiones' o 'atracciones'.")
        
input_string = input("Ingrese el tipo de información que desea obtener (colombia, departamentos, regiones, atracciones): ")  

obtener_informacion(input_string.lower())