#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
import codecs,sys
import cgi
import model_product

print("Content-Type: text/html; charset=utf-8\n")

sys.stdout.flush()

Product_List = model_product.getList()

msg = """<form name="表單" method="post" action="add_to_cart.py">"""

for (pID, name, price, stock) in Product_List:
    msg += f" 商品 : {name} 商品價格 : {price} 庫存 : {stock} " 
    msg += f""" <select name="amount_{pID}"><option value="0"> 0 </option> """
    for i in range(stock+1):
        msg += f""" <option value="{i}"> {i} </option> """
        i += 1
    
    msg += """ </select> """
    msg += """ </p> """

msg += """ <input type="submit" value="加入購物車"></form> """

with open("ShoppingPage.html","rb") as ShoppingPage:
    st = ShoppingPage.read()
    st = st.replace(b"###msg###", msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()