#!/bin/bash
set -e

if [ -f .env ]; then
    export $(grep -E '^STREAMLIT_PORT=' .env | xargs)
fi
PORT=${STREAMLIT_PORT:-${PORT:-8501}}
APP_FILE=${APP_FILE:-src/chatbot_interface/chatbot_UI.py}

exec streamlit run "$APP_FILE" --server.port="$PORT" --server.address=0.0.0.0