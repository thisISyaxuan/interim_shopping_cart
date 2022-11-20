#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
import codecs,sys
import cgi
import model_product

print("Content-type:text/html; charset;utf-8\n")

sys.stdout.flush()

Product_List = model_product.getList()

msg = """ <form name="表單" method="post" action="add_product.py">請輸入新商品資訊 """
msg += f""" </p> """

msg += f"""<input placeholder="名稱" name="name">"""
msg += f"""<input placeholder="價格" name="price">"""
msg += f"""<input placeholder="數量" name="amount"></p>"""

msg += """ <input type="submit" value="新增商品"></form>"""

with open("manager.html","rb") as manager:
    st = manager.read()
    st = st.replace(b"###msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()