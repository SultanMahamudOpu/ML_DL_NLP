from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# two sentence
s1 = 'I love programming in Python'
s2 = 'Python is my passion'
# One different sencetnce
s3 = 'I enjoy eating pizza'

emb1 = model.encode(s1)
emb2 = model.encode(s2)
emb3 = model.encode(s3)

# value যত 1 এর কাছাকাছি এত বেশি similer
print(util.cos_sim(emb1, emb2))
print(util.cos_sim(emb1, emb3))