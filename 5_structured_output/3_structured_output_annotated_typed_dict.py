from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

load_dotenv()

model=ChatOpenAI()


class Review(TypedDict):
    key_themes:Annotated[str,"Write down all the key themes discussed in the review in a list. "]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal['pos','neg'], "Return sentiment of the review either positive or negative"]
    pros:Annotated[Optional[list[str]],"Write down all the pros inside a list. "]
    cons:Annotated[Optional[list[str]],"Write down all the cons inside a list. "]

structured_model=model.with_structured_output(Review)
result=structured_model.invoke("Built quality is sturdy, a value-for-money product. Lightweight and portable. The power plug and Cord are also of a good quality, and the length of the cord is 1.5 meters (mentioned on the outer box). Easy to use and does not smell, even when using it for the first time after opening, it starts heating the room after 10-15 minutes. Must have a product for winter.")

print(result)