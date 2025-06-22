#!/bin/sh

echo starting ollama server...

ollama serve &
SERVE_PID=$!

echo "Waiting for Ollama server to start..."
max_retries=30
count=0
while ! ollama list >/dev/null 2>&1; do
  sleep 2
  count=$((count + 1))
  if [ $count -ge $max_retries ]; then
    echo "Ollama server failed to start after $max_retries attempts."
    exit 1
  fi
  echo "Waiting for Ollama server to start... (attempt $count)"
done

echo "Ollama server started successfully."
ollama pull llama3.1:8b

wait $SERVE_PID