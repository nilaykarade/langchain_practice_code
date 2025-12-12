from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

nilay:Person={'name':'nilay','age':42}

print(nilay)