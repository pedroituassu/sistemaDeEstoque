import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="vexH5Ac$Pc&x39%!Gyd1",
    database="sistemaDeEstoque"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS sistemaDeEstoque")

mycursor.execute("USE sistemaDeEstoque")

mycursor.execute("CREATE TABLE IF NOT EXISTS produtos ("
                 "ID INT AUTO_INCREMENT PRIMARY KEY,"
                 "hash VARCHAR(255) UNIQUE NOT NULL,"
                 "category VARCHAR(255),"
                 "brand VARCHAR(255),"
                 "name VARCHAR(255),"
                 "expirationTime INT(255),"
                 "minSupply INT(255),"
                 "maxSupply INT(255))"
                 )

mycursor.close()
mydb.close()