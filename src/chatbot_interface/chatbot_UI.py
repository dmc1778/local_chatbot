import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.core.ollama import OllamaChatInterface

ollama_object = OllamaChatInterface()

st.set_page_config(page_title="Local Chatbot", layout="wide")
st.title("🤖 Local Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_box = st.empty()
        full_response = ""
        for chunk in ollama_object.chat(prompt):
            full_response += chunk
            message_box.markdown(full_response + "▌")
        message_box.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
