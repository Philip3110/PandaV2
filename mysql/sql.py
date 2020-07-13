import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qaz321qaz"
)
cur = mydb.cursor()
cur.execute('DROP TABLE IF Panda;')

DB_Name = 'panda'
TABLES = {}

sql = """CREATE TABLE SHOP (

         Chips CHAR(20) NOT NULL,

         Chocolates CHAR(20),

         Cooldrinks CHAR(20),  

         Cupcakes CHAR(20),

         Fruit CHAR(20),

         Pies CHAR(20),

         Veggies CHAR(20), )"""

cur.execute(sql)
mydb.close()
print(mydb)
