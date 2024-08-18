import streamlit as st
from llama_parse import LlamaParse
import os, sys, tempfile, time

sys.path.append(os.getcwd())
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from app.agents.llamaparse import LlamaParseAgent

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

st.set_page_config(page_title="File Chatbot")

@st.cache_resource(show_spinner=False)
def parser(file_path):
    agent_instance = LlamaParseAgent(file_path)
    response = agent_instance.actor()
    return response    

def main():
    response = None
    begin = time.time()
    with st.sidebar:
        st.title("File Chatbot")
        st.write("Upload a File file to chat with the bot")
        st.subheader("Your file")
        file = st.file_uploader("Upload your File here and click on 'Process")

        if st.button("Process"):
            temp_dir = tempfile.mkdtemp()
            file_path = os.path.join(temp_dir, file.name)
            with open(file_path, "wb") as f:
                f.write(file.getvalue())

            response = parser(file_path)
            st.session_state.conversation = response

            st.success(
                "Document is successfully uploaded. You can ask questions!"
            )

    st.title("Chat with complex File")
    if response != None:
        end = time.time()
        st.write(f"Time taken: {end - begin}")
        st.write(response)
        

if __name__ == "__main__":
    main()