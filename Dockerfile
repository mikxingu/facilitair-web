# Usa a versão correta do Python (Heroku rodava em 3.10.9)
FROM python:3.10.9

# Instala bibliotecas do sistema antes de rodar o pip
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    build-essential \
    gfortran \
    libatlas-base-dev \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia apenas o requirements.txt primeiro para otimizar o cache
COPY requirements.txt /app/

# Instala numpy, pandas e lxml primeiro (pacotes pesados)
RUN pip install --no-cache-dir --prefer-binary numpy==1.23.0 pandas==1.4.3 lxml==4.9.0

# Agora instala o restante dos pacotes
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . /app

# Expor a porta da aplicação
EXPOSE 5000

# Comando correto para rodar o FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]