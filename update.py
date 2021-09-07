#!C:\Users\HARSHAD\AppData\Local\Programs\Python\Python39\python.exe
print ("Content-Type: text/html; charset=utf-8\n\n")
import cgi, cgitb 
cgitb.enable()
form=cgi.FieldStorage()
lid=form.getvalue('lid')
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
qr='update lang set name=%s,duration=%s,fees=%s,trainer=%s where id=%s'
val=(name,duration,fees,trainer,lid)
cr.execute(qr,val)
db.commit()
if cr.rowcount>0:
	print("<script>window.alert('Lanaguge sucessfully updated');</script>")
	print("<script>window.location.href='show.py';</script>")
else:
	print("<script>window.alert('Not updated');</script>")
	print("<script>window.location.href='show.py';</script>")