from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_documents=[
    "it's quite cold here",
    "I love coding",
    "Ai is quite intresting"
]

doc_embedings=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

result=doc_embedings.embed_documents(text_documents)

print(result)

print(type(result))