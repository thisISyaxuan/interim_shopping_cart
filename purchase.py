#!"C:\Users\軒\AppData\Local\Programs\Python\Python38\python.exe"
import codecs, sys
import cgi
import model_cart, model_product

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

print("Content-Type: text/html; charset=utf-8\n")

money = model_cart.purchase()

print("總金額", money, "元")
print("<br>")
print("<br> 結帳完成，謝謝惠顧")
print("<br>")
print("<br> <a href='ShoppingPage_control.py'> 繼續購物 </a>")