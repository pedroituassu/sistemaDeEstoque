import mysql.connector
from system_classes import Product

def add_product(product: Product):
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


def list_products():
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


def delete_product(item_hash):
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
