# Usar una imagen base con soporte para CUDA si es necesario
FROM nvidia/cuda:11.8.0-base-ubuntu22.04

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    git \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Instalar Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Exponer el puerto 8080 para el endpoint
EXPOSE 8080

# Comando para iniciar Ollama y exponer el endpoint
CMD ["ollama", "serve", "--host", "0.0.0.0:8080"]