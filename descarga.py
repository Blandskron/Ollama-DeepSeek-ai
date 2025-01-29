import subprocess

# Comando para descargar el modelo desde Ollama
model_name = "deepseek-r1:1.5b"

# Ejecutar el modelo usando el cliente de Ollama desde Python
# Asumimos que Ollama está correctamente instalado en tu sistema
command = f"ollama pull {model_name}"

# Ejecutar el comando en la terminal para descargar el modelo
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Obtener la salida del proceso
stdout, stderr = process.communicate()

# Ver si hay errores al intentar descargar el modelo
if process.returncode == 0:
    print(f"Modelo {model_name} descargado exitosamente.")
else:
    print(f"Error al descargar el modelo: {stderr.decode()}")
