from pydantic import BaseModel

# Product Model
class Product(BaseModel):
    hash: str
    category: str
    brand: str
    name: str
    expirationTime: int
    minSupply: int
    maxSupply: int