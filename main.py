import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st


# Model Loading
def load_model(model_name):
    print(f"Loading model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name,
                                                 torch_dtype=torch.float16,
                                                 device_map="auto")
    print("Model loaded successfully!")
    return tokenizer, model


def generate_response(model, tokenizer, prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_length=max_length, num_return_sequences=1, do_sample=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Streamlit Interface
def run_streamlit_app(model, tokenizer):
    st.title("Medical Student LLaMA 2 Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is your medical question?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = generate_response(model, tokenizer, prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)


# Main execution
if __name__ == "__main__":
    model_name = "meta-llama/Llama-2-7b-chat-hf"

    tokenizer, model = load_model(model_name)

    print("Starting Streamlit app...")
    run_streamlit_app(model, tokenizer)
