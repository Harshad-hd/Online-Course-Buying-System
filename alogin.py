#!C:\Users\HARSHAD\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html; charset=utf-8\n\n")
import cgi, cgitb
cgitb.enable()
form=cgi.FieldStorage()
uid=form.getvalue('id')
pwd=form.getvalue('pwd')
if uid=='admin' and pwd=='12345':
	print("<script>window.location.href='adminhome.html';</script>")
else:
	print("<script>window.alert('Invalid id and password');</script>")
	print("<script>window.location.href='index.html';</script>")