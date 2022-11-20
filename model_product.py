#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
from dbConfig import conn, cur
import model_cart

def getList():
    sql = "SELECT * FROM `product` WHERE `stock` > 0;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def search(pID):
    sql = "SELECT * FROM `product` WHERE `pID` = %s;"
    cur.execute(sql, (pID,))
    records = cur.fetchall()
    # name, price, stock
    return records[0][1], records[0][2], records[0][3]

def stock_after_paid(pID, quantity):
    sql = "UPDATE `product` SET `stock`=`stock`-%s WHERE `pID` = %s;"
    cur.execute(sql, (quantity, pID,))
    cur.fetchall()

def add_product(name, price, stock):
    if(name == None or price == None or stock == None):
        return False
    sql = "insert into product (name, price, stock) values (%s,%s,%s);"
    cur.execute(sql,(name, price, stock))
    conn.commit()
    return True

def changeName(name, pID):
    if(name == None):
        return
    else:
        sql = "update product set name=%s where pID=%s;"
        cur.execute(sql,(name, pID))
        conn.commit()

def changePrice(price, pID):
    if(price == None):
        return
    else:
        sql = "update product set price=%s where pID=%s;"
        cur.execute(sql,(price, pID))
        conn.commit()

def changeStock(stock, pID):
    if(stock == None):
        return
    elif(stock == '0'):
        sql = "DELETE FROM `product` WHERE `product`.`pID` = %s;"
        cur.execute(sql,(pID,))
        conn.commit()
    else:
        sql = "update product set stock=%s where pID=%s;"
        cur.execute(sql,(stock, pID))
        conn.commit()
    return True