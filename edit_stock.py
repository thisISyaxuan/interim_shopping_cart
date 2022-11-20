#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import model_product

print("Content-Type: text/html; charset=utf-8\n")

Product_List = model_product.getList()
form = cgi.FieldStorage()

for i in range(Product_List[len(Product_List)-1][0]):
    i += 1
    stock = form.getvalue(f'amount_{i}')
    model_product.changeStock(stock, i)
    price = form.getvalue(f'price_{i}')
    model_product.changePrice(price, i)
    name = form.getvalue(f'name_{i}')
    model_product.changeName(name, i)

print("更新成功！")
print("<br><a href='manager_log_in.html'> 查看管理頁面 </a>")
