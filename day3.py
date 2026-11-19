from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field

app= FastAPI()

class ProductRequest(BaseModel):
    name:str=Field(min_length=3,max_length=50)
    price:float
    quantity:int |None=None
    age: int=Field(ge=18)
    available:bool = Field(max_length=60) 

class Product(BaseModel):
    price: float=Field(gt=100)
    quantity: float= Field(le=50)
    