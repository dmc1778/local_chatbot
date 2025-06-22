#!/bin/sh

chmod +x ./docker/streamlit/streamlit_entrypoint.sh
chmod +x ./docker/ollama/ollama_entrypoint.sh

sudo docker-compose down
sudo docker-compose build
sudo docker-compose up