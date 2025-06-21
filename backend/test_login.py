import requests
import time

url = "http://127.0.0.1:8000/api/login/"
data = {
    "username": "liz",  # Usa tu superusuario
    "password": "liza"  # Reemplaza con la real
}

try:
    response = requests.post(url, json=data, timeout=5)  # Timeout de 5 segundos
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except requests.exceptions.ConnectionError:
    print("Error: ¿Está corriendo el servidor Django? Ejecuta: python manage.py runserver")
except Exception as e:
    print("Error inesperado:", str(e))