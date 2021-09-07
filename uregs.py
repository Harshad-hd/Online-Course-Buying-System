#!C:\Users\HARSHAD\AppData\Local\Programs\Python\Python39\python.exe
print ("Content-Type: text/html; charset=utf-8\n\n")
import cgi, cgitb 
cgitb.enable()
form=cgi.FieldStorage()
name=form.getvalue('name')
email=form.getvalue('email')
pwd=form.getvalue('pwd')
import mysql.connector
db=mysql.connector.connect(
	host='localhost',
	database='py530',
	user='root',
	password='root'
	)
cr=db.cursor()
qr='insert into student values(%s,%s,%s)'
val=(name,email,pwd,)
cr.execute(qr,val)
db.commit()
if cr.rowcount>0:
	print("<script>window.alert('Student sucessfully added');</script>")
	print("<script>window.location.href='index.html';</script>")
else:
	print("<script>window.alert('Not added');</script>")
	print("<script>window.location.href='uregs.html';</script>")