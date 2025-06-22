FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git /app/

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ADD ./docker /app/docker

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

RUN chmod +x /app/docker/streamlit/streamlit_entrypoint.sh
RUN chmod +x /app/docker/ollama/ollama_entrypoint.sh