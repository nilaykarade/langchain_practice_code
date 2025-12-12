from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

model=ChatOpenAI()


class Review(BaseModel):
    key_themes:list[str]=Field(description="Write down all the key themes discussed in the review in a list.")
    summary:str=Field(description="A brief summary of the review")
    sentiment:Literal['pos','neg']=Field(description="Return sentiment of the review either positive or negative")
    pros:Optional[list[str]]=Field(default=None, description="Write down all the pros inside a list.")
    cros:Optional[list[str]]=Field(default=None, description="Write down all the cons inside a list.")
    names:Optional[str]=Field(default=None,description="Write the name of the reviwer.")

structured_model=model.with_structured_output(Review)
result=structured_model.invoke("Built quality is sturdy, a value-for-money product. Lightweight and portable. The power plug and Cord are also of a good quality, and the length of the cord is 1.5 meters (mentioned on the outer box). Easy to use and does not smell, even when using it for the first time after opening, it starts heating the room after 10-15 minutes. Must have a product for winter.")

for item in result:
    print(item)
    