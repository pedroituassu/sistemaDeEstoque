from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from system_classes import Product
from database import db_functions as db

app = FastAPI()


# Example Endpoint
@app.get("/")
def read_root():
    return {"message": "Storage System API is running!"}

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
    db.add_product(product)
    return {"message": "Produto criado com sucesso!", "product": product}


# Endpoint to get all products
@app.get("/products/")
def get_products():
    return db.list_products()

@app.get("/products/{product_hash}")
def get_product(product_hash: str):
    return db.get_product_by_hash(product_hash)

@app.put("/products/{product_hash}")
def edit_product(product_hash: str, product: Product):
    db.edit_product(product_hash, product)
    return {"message": "Produto editado com sucesso!", "product": product}

@app.delete("/products/{product_hash}")
def delete_product(product_hash: str):
    db.delete_product(product_hash)
    return {"message": "Produto deletado com sucesso!"}
