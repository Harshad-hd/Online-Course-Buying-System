#!C:\Users\HARSHAD\AppData\Local\Programs\Python\Python39\python.exe
print ("Content-Type: text/html; charset=utf-8\n\n")
import cgi, cgitb 
cgitb.enable()
print("<a href='index.html'>Logout</a>")
import mysql.connector
db=mysql.connector.connect(
	host='localhost',
	database='py530',
	user='root',
	password='root'
	)
cr=db.cursor()
qr='select * from lang'
cr.execute(qr)
data=cr.fetchall()
data=tuple(data)
for lid,name,duration,fees,trainer in data:
	print("<div style='height: 150px;width: 100%;background-color: pink;text-align: center'>")
	print("ID:",lid,"<br>")
	print("NAME:",name,"<br>")
	print("DURATION:",duration,"<br>")
	print("FEES:",fees,"<br>")
	print("TRAINER:",trainer,"<br>")
	print("<a href='https://www.paypal.com/in/signin'>BUY COURSE</a>")
	print("</div>")
	