from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model= 'gemini-embedding-2'
)

vector = embeddings.embed_documents([
    'Today is Monday',
    'Today is Sunday',
    'Today is April Fools day',
    'I am Sultan'
])

# print(len(vector), len(vector[0]))
# print(len(vector), len(vector[1]))
print(len(vector), len(vector[3]))