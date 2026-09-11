from langchain_huggingface import HuggingFaceEmbeddings

# এখানে আমারা local model use করতেছি, তাই api key লাগে নাই, dotenv ও লাগে নাই
embedding = HuggingFaceEmbeddings( 
    model = 'sentence-transformers/all-MiniLM-L6-v2'
)

documents = [
    'I love AI',
    'I love ML',
    'I love DL',
]

vector = embedding.embed_documents(documents)

# print(len(vector))
print(vector)