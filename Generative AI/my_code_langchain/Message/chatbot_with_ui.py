from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

st.header('My Chatbot')
# chatbot
user_input = st.chat_input('Type your message')

if user_input:
    if user_input.strip().lower() == 'exit':
        st.stop() # যে ভাবেই exit লিখাটা দিক, session stop হয়ে যাবে
        
    with st.chat_message('user'):
        st.write(user_input)
        
    result = model.invoke(user_input)
    
    with st.chat_message('assistant'):
        st.write(result.content)