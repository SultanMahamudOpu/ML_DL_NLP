from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    # model= 'qwen/qwen3.6-27b',
    model= 'openai/gpt-oss-120b'
)

result= llm.invoke('What it he Capital of BD?')
print(result.content)