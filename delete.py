#!C:\Users\HARSHAD\AppData\Local\Programs\Python\Python39\python.exe
print ("Content-Type: text/html; charset=utf-8\n\n")
import cgi, cgitb 
cgitb.enable()
form=cgi.FieldStorage()
lid=form.getvalue('lid')
import mysql.connector
db=mysql.connector.connect(
	host='localhost',
	database='py530',
	user='root',
	password='root'
	)
cr=db.cursor()
qr='delete from lang where id=%s'
val=(lid,)
cr.execute(qr,val)
db.commit()
if cr.rowcount>0:
	print("<script>window.alert('Lanaguge sucessfully deleted');</script>")
	print("<script>window.location.href='show.py';</script>")
else:
	print("<script>window.alert('Not deleted');</script>")
	print("<script>window.location.href='show.py';</script>")