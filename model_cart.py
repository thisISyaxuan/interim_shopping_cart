#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
import model_product
from dbConfig import conn, cur

def add_to_cart(pID, want):
    if (want == None):
        return
    # 購物車還沒有這項商品 => insert
    if (exist(pID) == []):
        insert_sql = "INSERT INTO `cart`(`uID`, `pID`, `quantity`) VALUES ('1','%s','%s');"
        cur.execute(insert_sql, (pID, want,))
        conn.commit()
    # 購物車已經有這項商品 => update
    else:
        update_sql="UPDATE `cart` SET `quantity`=%s WHERE `pID` = %s;"
        cur.execute(update_sql, (want, pID,))
        conn.commit()
    return True

def exist(pID):
    sql = "SELECT `pID` FROM `cart` WHERE `pID` = %s;"
    cur.execute(sql, (pID, ))
    records = cur.fetchall()
    return records

def getList():
    sql = "SELECT * FROM `cart` WHERE 1;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def purchase():
    sql = "SELECT * FROM `cart` WHERE `quantity` > 0 and `uID` = 1 and `status` = 0;"
    cur.execute(sql)
    records = cur.fetchall()
    money = 0
    for (cID, uID, pID, quantity, status) in records:
        name, price, stock = model_product.search(pID)
        money += (price*quantity)
        model_product.stock_after_paid(pID, quantity)
        update_status(cID)
    return money

def update_status(cID):
    sql = "UPDATE `cart` SET `status`='1' WHERE `cID` = %s;"
    cur.execute(sql, (cID,))
    cur.fetchall()
