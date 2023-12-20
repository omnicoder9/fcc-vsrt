import pymongo

#client = ...
db = client.sample_mflix
collection = db.movies

print(collection.find().limit(5))

#https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
#12:51, https://www.youtube.com/watch?v=JEBDfGqrAUA