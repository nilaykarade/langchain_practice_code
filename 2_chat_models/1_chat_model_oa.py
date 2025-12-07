import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("gpt-4.1")
response = model.invoke("what is the capital of India")
print(response.content)

# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model=ChatOpenAI(model='gpt-4o-mini',temperature=0.1,max_completion_tokens=10)
# result=model.invoke('what is the capital of India')

# print(result.content)