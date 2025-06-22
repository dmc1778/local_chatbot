# Ollama Chatbot

This project provides a Python interface to interact with the Ollama API. It allows you to chat with models, manage your local models, and pull models from the Ollama registry.

## Features

- Chat with a model (streaming)
- List local models
- Get model information
- Pull a model from the registry

## API

The `OllamaChatInterface` class in `src/core/ollama.py` provides the following methods:

- `chat(user_message: str)`: Chat with a model. Returns a generator that yields the response in chunks.
- `list_models()`: List all local models.
- `get_model_info(model_name: str)`: Get information about a specific model.
- `pull_model(model_name: str)`: Pull a model from the Ollama registry. Returns a generator that yields the status of the download.
