from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=256)

text_data=[
    "pandas is used for data anaylsis, data cleaning techniques like removing null values, outliers, duplicates from the data.",
    "seaborn is a library used for data visualization. We can draw vairous plots like scaaterplot, lineplot, heatmap, histogram for understading patterns from the data.",
    "sklearn is an important library to develop machine learning models, make predictions and evaulate model performance."
    "PyTorch is a useful for developing deep models like ann, cnn, rnn for unstructured data"

]
doc_embeddings=embeddings.embed_documents(text_data)

query="explain what is used to draw heatmap plot"
query_embeddings=embeddings.embed_query(query)

similarity_scores=cosine_similarity([query_embeddings],doc_embeddings)

#2D numpy array with similarity scores
print(similarity_scores)
print(type(similarity_scores))

#consider 1st element i.e. array with 3 sim scores
similarity_scores=similarity_scores[0]

#create a list of enumerated scores, sort them and pick up the last vaue at index -1 being the highest sim score 
index, score=sorted(list(enumerate(similarity_scores)),key=lambda x:x[1])[-1]

print("Query",query)
print("Score:",score)
print(text_data[index])