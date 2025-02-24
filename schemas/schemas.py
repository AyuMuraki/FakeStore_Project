from pydantic import BaseModel
from typing import Optional

#Classe utilizada como representacao do modelo de produto.

class RatingSchema(BaseModel):
    rate: float
    count: int

class ProductSchema(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: Optional[RatingSchema] = None 
    
