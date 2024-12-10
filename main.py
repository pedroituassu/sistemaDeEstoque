from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Date Model
class Date(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int

# Product Model
class Product(BaseModel):
    id: str
    name: str
    expirationTime: int
    minSupply: int
    maxSupply: int
    category: str
    brand: str

# ItemMovement Model
class ItemMovement(BaseModel):
    product: Product
    amount: int

# Purchase Model
class Purchase(BaseModel):
    items: List[ItemMovement]
    itemAmount: int
    description: str
    date: Date
    type: str
    receiver: Optional[str]

# Delivery Model
class Delivery(BaseModel):
    items: List[ItemMovement]
    itemAmount: int
    description: str
    date: Date
    sender: Optional[str]

# Client Model
class Client(BaseModel):
    name: str
    cpf: int
    email: str
    cellphone: int
    password: str
    purchases: List[Purchase]

# Provider Model
class Provider(BaseModel):
    name: str
    cpf: int
    email: str
    cellphone: int
    password: str
    company: str
    cnpj: int
    deliveries: List[Delivery]

# Admin Model
class Admin(BaseModel):
    name: str
    cpf: int
    email: str
    cellphone: int
    password: str
    registration: int

products_db = []

# Example Endpoint
@app.get("/")
def read_root():
    return {"message": "Storage System API is running!"}

@app.get("/clients")
def get_clients():
    # Here you can mock data or connect to a database
    example_client = Client(
        name="John Doe",
        cpf=123456789,
        email="john.doe@example.com",
        cellphone=987654321,
        password="securepassword",
        purchases=[],
    )
    return [example_client]


# Allow all origins for development purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can limit this to your React app's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint to create a new product
@app.post("/products/")
def create_product(product: Product):
    products_db.append(product)
    return {"message": "Produto criado com sucesso!", "product": product}

# Endpoint to get all products
@app.get("/products/")
def get_products():
    return products_db

@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    global products_db
    for product in products_db:
        if product.id == product_id:
            products_db.remove(product)
            return {"message": "Produto deletado com sucesso!", "product": product}
    raise HTTPException(status_code=404, detail="Product not found")
