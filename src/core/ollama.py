from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()

OLLAMA_HOST_URL = os.getenv("OLLAMA_HOST_URL")

if not OLLAMA_HOST_URL:
    raise EnvironmentError("BASE_URL environment variable is not set.")

class OllamaChatInterface:
    def __init__(self):
        self.base_url = OLLAMA_HOST_URL
        self.model_name = "llama3.1:8b"
        
    def chat(self, user_message: str):
        url = f'{self.base_url}/api/chat'
        
        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "stream": True
        }
        
        try:
            response = requests.post(url, data=json.dumps(payload), stream=True)
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    decoded_line = json.loads(line.decode('utf-8'))
                    yield decoded_line.get("message", {}).get("content", "")
            
        except requests.exceptions.RequestException as e:
            yield f"An error occurred: {e}"

    def list_models(self):
        try:
            response = requests.get(f'{self.base_url}/api/tags')
            response.raise_for_status()
            return response.json()["models"]
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

    def get_model_info(self, model_name: str):
        url = f'{self.base_url}/api/show'
        
        payload = {
            "name": model_name
        }
        
        try:
            response = requests.post(url, data=json.dumps(payload))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

    def pull_model(self, model_name: str):
        url = f'{self.base_url}/api/pull'
        
        payload = {
            "name": model_name,
            "stream": True
        }
        
        try:
            response = requests.post(url, data=json.dumps(payload), stream=True)
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    decoded_line = json.loads(line.decode('utf-8'))
                    yield decoded_line
            
        except requests.exceptions.RequestException as e:
            yield f"An error occurred: {e}"