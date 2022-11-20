#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import model_product

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

status = model_product.add_product(form.getvalue(f'name'), form.getvalue(f'price'), form.getvalue(f'amount'))
if(status == False):
    print("資料未輸入齊全")

print("更新成功！")
print("<br><a href='manager_log_in.html'> 查看管理頁面 </a>")