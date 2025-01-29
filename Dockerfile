# Usamos una imagen base de Ubuntu sin CUDA
FROM ubuntu:22.04

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    git \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Instalar Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Verificar si la instalación de Ollama se realizó correctamente
RUN ollama --version

# Instalar el modelo deepseek-r1:1.5b
RUN ollama run deepseek-r1:1.5b || echo "El modelo Deepseek no se puede instalar automáticamente"

# Exponer el puerto 8080 para el endpoint
EXPOSE 8080

# Comando para iniciar Ollama y exponer el endpoint
CMD ["ollama", "serve", "--host", "0.0.0.0:8080"]
