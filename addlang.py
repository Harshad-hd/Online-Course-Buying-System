#!C:\Users\HARSHAD\AppData\Local\Programs\Python\Python39\python.exe
print ("Content-Type: text/html; charset=utf-8\n\n")
import cgi, cgitb 
cgitb.enable()
form=cgi.FieldStorage()
lid=form.getvalue('id')
name=form.getvalue('name')
duration=form.getvalue('duration')
fees=form.getvalue('fees')
fees=int(fees)
trainer=form.getvalue('trainer')
import mysql.connector
db=mysql.connector.connect(
	host='localhost',
	database='py530',
	user='root',
	password='root'
	)
cr=db.cursor()
qr='insert into lang values(%s,%s,%s,%s,%s)'
val=(lid,name,duration,fees,trainer,)
cr.execute(qr,val)
db.commit()
if cr.rowcount>0:
	print("<script>window.alert('Lanaguge sucessfully added');</script>")
	print("<script>window.location.href='adminhome.html';</script>")
else:
	print("<script>window.alert('Not added');</script>")
	print("<script>window.location.href='index.html';</script>")