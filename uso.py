import subprocess

# Nombre del modelo
model_name = "deepseek-r1:1.5b"

while True:
    # Solicitar al usuario la entrada
    input_text = input("Escribe algo para preguntar al modelo (o 'salir' para terminar): ")
    
    # Si el usuario quiere salir del bucle, termina
    if input_text.lower() == "salir":
        print("Saliendo...")
        break
    
    # Ejecutar el modelo con Ollama
    command = f"ollama run {model_name} {input_text}"

    # Ejecutar el comando en la terminal
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Obtener la salida del proceso
    stdout, stderr = process.communicate()

    # Mostrar el resultado
    if process.returncode == 0:
        print(f"Respuesta del modelo: {stdout.decode()}")
    else:
        print(f"Error al ejecutar el modelo: {stderr.decode()}")
