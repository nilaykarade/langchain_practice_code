from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model=ChatOpenAI()


class Review(TypedDict):
    summary:str
    sentiment:str

structured_model=model.with_structured_output(Review)
result=structured_model.invoke("Well, the hardware seems to be good as per the numbers. But the phone comes with a lot of pre-installed unnecessary apps that cause a lot of storage. Phone also seems to have heating issues and slow charging.")

print(result)