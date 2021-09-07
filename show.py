#!C:\Users\HARSHAD\AppData\Local\Programs\Python\Python39\python.exe
print ("Content-Type: text/html; charset=utf-8\n\n")
import cgi, cgitb 
cgitb.enable()
import mysql.connector
db=mysql.connector.connect(
	host='localhost',
	database='py530',
	user='root',
	password='root'
	)
cr=db.cursor()
qr='select * from lang'
cr.execute(qr,)
data=cr.fetchall()
data=tuple(data)
print("<table align='center' border='1px'>")
for lid,name,duration,fees,trainer in data:
	print("<tr>")
	print("<form action='update.py'>")
	print("<td>")
	print("<input type='text' name='lid' value="+lid+" readonly />")
	print("</td>")
	print("<td>")
	print("<input type='text' name='name' value="+name+" />")
	print("</td>")
	print("<td>")
	print("<input type='text' name='duration' value="+duration+" />")
	print("</td>")
	print("<td>")
	print("<input type='number' name='fees' value="+str(fees)+" />")
	print("</td>")
	print("<td>")
	print("<input type='text' name='trainer' value="+trainer+" />")
	print("</td>")
	print("<td>")
	print("<input type='submit' value='Update' />")
	print("</td>")
	print("</form>")
	print("<td>")
	print("<form action='delete.py'>")
	print("<input type='hidden' name='lid' value="+lid+" />")
	print("<input type='submit' value='delete' />")
	print("</form>")
	print("</td>")
	print("</tr>")
print("</table>")