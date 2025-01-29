import requests

# URL del endpoint
url = "http://localhost:8080/api/generate"

# Datos que se enviarán en el cuerpo de la solicitud (en formato JSON)
data = {
    "model": "deepseek-r1:1.5b",
    "prompt": "Hola, ¿cómo estás?"
}

# Encabezados de la solicitud (opcional, pero recomendado para especificar el tipo de contenido)
headers = {
    "Content-Type": "application/json"
}

# Realizar la solicitud POST
response = requests.post(url, json=data, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Imprimir la respuesta del servidor
    print("Respuesta del servidor:")
    print(response.json())
else:
    # Imprimir el código de estado si la solicitud no fue exitosa
    print(f"Error: {response.status_code}")
    print(response.text)
    