from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# memory
chat_history = [SystemMessage(content= 'You are a helpful assistant. Always answer in a short paragraph(2-4 sentence)')]

# Terminal chatbot
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input == 'exit':
        break
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    
    print('AI: ', result.content)
    
print('Printing chat history', chat_history)