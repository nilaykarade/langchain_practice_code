import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
response = model.invoke("Why do parrots talk?")
print(response.content)


# from langchain_google_genai import ChatGoogleGenerativeAI
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = ChatGoogleGenerativeAI(
#     model="gemini-1.5-pro",    # or gemini-1.5-pro
# )


# result=model.invoke('what is the capital of India')

# print(result.content)