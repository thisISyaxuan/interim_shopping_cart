#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
import codecs,sys
import cgi
import model_product

print("Content-type:text/html; charset;utf-8\n")

sys.stdout.flush()

Product_List = model_product.getList()

msg = """ <form name="表單" method="post" action="edit_stock.py"> 輸入想調整的內容 """
msg += f""" </p> """
for (pID, name, price, stock) in Product_List:
    msg += f"編號 : {pID} 商品 : {name} 商品價格 : {price} 庫存 : {stock} " 
    msg += f""" </p> """
    msg += f""" <input placeholder="更改名稱" name="name_{id}"> """
    msg += f""" <input placeholder="更改價格" name="price_{id}"> """
    msg += f""" <input placeholder="更改庫存" name="amount_{id}"> """
    msg += f""" </p> """

msg += """ <input type="submit" value="送出修改"></form> """
msg += f""" </p> """

with open("manager.html","rb") as manager:
    st = manager.read()
    st = st.replace(b"###msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()