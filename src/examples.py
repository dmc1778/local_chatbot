from core.ollama import OllamaChatInterface

def run_examples():
    ollama_connector = OllamaChatInterface()

    print("Available models:")
    models = ollama_connector.list_models()
    if isinstance(models, list) and models:
        for model in models:
            print(f"- {model['name']}")
        
        first_model_name = models[0]['name']
        print(f"\nGetting info for model: {first_model_name}")
        model_info = ollama_connector.get_model_info(first_model_name)
        # print(model_info)

    else:
        print(models)
    print("-" * 20)
    
    user_message = "why human body needs blood?"
    response_stream = ollama_connector.chat(user_message)
    for chunk in response_stream:
        print(chunk, end="", flush=True)
    print()

    print("Pulling model 'gemma:2b':")
    pull_stream = ollama_connector.pull_model("gemma:2b")
    for chunk in pull_stream:
        print(chunk.get("status"))
    print("-" * 20)

    print("Deleting model 'gemma:2b':")
    delete_status = ollama_connector.delete_model("gemma:2b")
    if delete_status == 200:
        print("Model 'gemma:2b' deleted successfully.")
    else:
        print(f"Error deleting model: {delete_status}")
    print("-" * 20)


if __name__ == "__main__":
    run_examples() 