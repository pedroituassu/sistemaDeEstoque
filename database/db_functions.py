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

    sql = "INSERT INTO produtos (hash, category, brand, name, unitWeight, expirationTime, minSupply, maxSupply) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (product.hash, product.category, product.brand, product.name, product.unitWeight, product.expirationTime, product.minSupply, product.maxSupply)

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

    products = []
    for product in myresult:
        products.append(Product(hash=product[1], category=product[2], brand=product[3], name=product[4], unitWeight=product[5], expirationTime=product[6], minSupply=product[7], maxSupply=product[8]))

    mycursor.close()
    mydb.close()

    return products


def get_product_by_hash(product_hash: str):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="vexH5Ac$Pc&x39%!Gyd1",
        database="sistemaDeEstoque"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM produtos WHERE hash = %s", (product_hash,))
    myresult = mycursor.fetchone()

    product = Product(hash=myresult[1], category=myresult[2], brand=myresult[3], name=myresult[4], unitWeight=myresult[5], expirationTime=myresult[6], minSupply=myresult[7], maxSupply=myresult[8])

    mycursor.close()
    mydb.close()

    return product


def edit_product(old_product_hash: str, product: Product):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="vexH5Ac$Pc&x39%!Gyd1",
        database="sistemaDeEstoque"
    )
    mycursor = mydb.cursor()

    sql = "UPDATE produtos SET hash = %s, category = %s, brand = %s, name = %s, unitWeight = %s, expirationTime = %s, minSupply = %s, maxSupply = %s WHERE hash = %s"
    val = (product.hash, product.category, product.brand, product.name, product.unitWeight, product.expirationTime, product.minSupply, product.maxSupply, old_product_hash)
    mycursor.execute(sql, val)

    mydb.commit()

    mycursor.close()
    mydb.close()


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
