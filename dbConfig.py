#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
#import mariadb
import mysql.connector 

try:
    #conn = mariadb.connect(
    conn = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "",
        database="shopping_cart"
    )
except: #mariadb.Error as e:
    print("Error connecting to DB")
    exit(1)
cur=conn.cursor()