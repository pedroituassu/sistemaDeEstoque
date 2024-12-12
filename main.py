import mysql.connector

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Product Model
class Product(BaseModel):
    hash: str
    category: str
    brand: str
    name: str
    expirationTime: int
    minSupply: int
    maxSupply: int


def db_add_product(product: Product):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="vexH5Ac$Pc&x39%!Gyd1",
        database="sistemaDeEstoque"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO produtos (hash, category, brand, name, expirationTime, minSupply, maxSupply) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (product.hash, product.category, product.brand, product.name, product.expirationTime, product.minSupply, product.maxSupply)

    mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()
    mydb.close()


def db_list_products():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="vexH5Ac$Pc&x39%!Gyd1",
        database="sistemaDeEstoque"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM produtos"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    products =[]
    for product in myresult:
        products.append(Product(hash=product[1], category=product[2], brand=product[3], name=product[4], expirationTime=product[5], minSupply=product[6], maxSupply=product[7]))
    mycursor.close()
    mydb.close()

    return products


def db_delete_product(item_hash):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="vexH5Ac$Pc&x39%!Gyd1",
        database="sistemaDeEstoque"
    )
    mycursor = mydb.cursor()
    sql = "DELETE FROM produtos WHERE hash = %s"
    val = (item_hash,)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()

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
    db_add_product(product)
    return {"message": "Produto criado com sucesso!", "product": product}


# Endpoint to get all products
@app.get("/products/")
def get_products():
    return db_list_products()


@app.delete("/products/{product_hash}")
def delete_product(product_hash: str):
    db_delete_product(product_hash)
    return {"message": "Produto deletado com sucesso!"}
