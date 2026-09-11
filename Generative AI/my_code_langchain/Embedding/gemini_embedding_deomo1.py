from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model= 'gemini-embedding-2'
)

vector = embeddings.embed_query('What it the capital of BD')

# print(vector) # print full vector
# print(len(vector)) # print vector length
print(len(vector), vector[:5]) # print vector length and first 5 vectors