#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
import codecs,sys
import cgi
import model_cart, model_product

print("Content-type:text/html; charset;utf-8\n")

sys.stdout.flush()

Cart_List = model_cart.getList()

msg = """ <form name="表單" method="post"> """
Sum_Price = 0
sale = 0
for (cID, uID, pID, quantity, status) in Cart_List:
    if (quantity > 0 & status == 0):
        name, price, stock = model_product.search(pID)
        msg = msg + f" 商品 : {name} 單價 : {price} 購買數量 : {quantity} " 
        # 結帳購物車時，滿1000打八折，不滿1000打九折
        Sum_Price += (price*quantity)
        msg += """ </p> """ 

sale = Sum_Price
if (sale<1000):
    sale = sale*0.9
else:
    sale = sale*0.8

msg += f""" <p> 折扣：{sale} </p> """
msg += f""" </form> """
msg += f""" <p> 原價：{Sum_Price} </p> """
msg += f""" </form> """

with open("ShowCart.html", "rb") as ShowCart:
    st = ShowCart.read()
    st = st.replace(b"###msg###", msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()