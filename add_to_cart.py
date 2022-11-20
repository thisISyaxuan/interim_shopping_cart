#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
import codecs,sys
import cgi
import model_product, model_cart

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)


#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")

Product_List = model_product.getList()
form = cgi.FieldStorage()
for i in Product_List:
    pID = i[0]
    want = form.getvalue(f'amount_{pID}')
    status = model_cart.add_to_cart(pID, want)
    if(status != True):
        print(f"")

print("成功加入！")
print("<br><a href='ShowCart_control.py'> 查看購物車 </a>")
print("<br><a href='ShoppingPage_control.py'> 繼續購物 </a>")