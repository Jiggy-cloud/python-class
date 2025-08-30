print("Welcome to python database")

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    DATABASE = "ShaylaDB"
    )
mybaby = mydb.cursor()
mybaby.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255)) ")

# mybaby.execute("CREATE DATABASE ShaylaDB")
# mybaby.execute("SHOW DATABASES")
# for x in mybaby:
    # print(x)

    # new addition 
 def details():
     name = "Dammy Agbomabiwon"
     address = "Ikorodu"
     Print(nmae + address)

     details() 