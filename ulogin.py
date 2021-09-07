#!C:\Users\HARSHAD\AppData\Local\Programs\Python\Python39\python.exe
print ("Content-Type: text/html; charset=utf-8\n\n")
import cgi, cgitb 
cgitb.enable()
form=cgi.FieldStorage()
pwd=form.getvalue('pwd')
email=form.getvalue('email')
import mysql.connector
db=mysql.connector.connect(
	host='localhost',
	database='py530',
	user='root',
	password='root'
	)
cr=db.cursor()
qr='select * from student where email=%s and pwd=%s'
val=(email,pwd,)
cr.execute(qr,val)
data=cr.fetchall()
if len(data)>0:
	print("<script>window.location.href='userhome.py';</script>")
else:
	print("<script>window.alert('Invalid email and password');</script>")
	print("<script>window.location.href='index.html';</script>")