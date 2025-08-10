from pyfiglet import figlet_format
from termcolor import colored
fnt=figlet_format('DGA MOTORS')
print(fnt)
def home():
print(" =======================================")
print(" | SUCCESSFULLY LOGGED IN |")
print(" =======================================")
print(" ")
print(" =======================================")
print(" | DATABASES AVAILABLE IN THE SYSTEM |")
print(" =======================================")
print(" | 1.Customer |")
print(" | 2.Inventory |")
print(" | 3.Logout |")
print(" =======================================")
ch=int(input(" |enter your choice:"))
if ch==1:
print(" ")
Customer()
elif ch==2:
print(" ")
Inventory()
elif ch==3:
print(" =======================================")
print(" |Do you wish to logout? | ")
a=input(" | Y/N |")
if a=="N" or a=="n":
login()
elif a=="Y" or a=="y":
m=figlet_format('THANK YOU')
print(m)
else:
print(" =======================================")
print(" | incorrect value |")
print(" =======================================")
home()
else:
print(" =======================================")
print(" | incorrect value |")
print(" =======================================")
home()
def login():
print(" =======================================")
print(" | LOGIN PAGE |")
print(" =======================================")
print(" ")
username=input(" Enter your username ")
if username=="garv" or username=="armaan" or username=="dhruv" or username=="Garv" or username=="GARV" or
username=="Armaan" or username=="ARMAAN" or username=="Dhruv" or username=="DHRUV":
password=input(" enter the password ")
if password=="DGA1234":
home()
else:
print(" ")
print(" =======================================")
print(" Print incorrect password")
print(" Please Try Again")
print(" =======================================")
print(" ")
login()
else:
print(" ")
print(" =======================================")
print(" Incorrect username")
print(" Please Try Again")
print(" =======================================")
print(" ")
login()
def Customer():
print(" =======================================")
print(" | Database Customer |")
print(" =======================================")
print(" | |")
print(" | What do you wish to do? |")
print(" | 1.Add details of a new customer |")
print(" | 2. Update details of an old customer|")
print(" | 3.Delete records |")
print(" | 4.View records |")
print(" | 5.Return to homescreen |")
print(" =======================================")
ch=int(input(" |enter your choice:"))
if ch==1:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database=" dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
Cust_id=int(input(" |Enter the Customer ID: "))
Cust_name=input(" |Enter Customer name: ")
Cust_address=input(" |Enter Customer address: ")
Phone_no=int(input(" |Enter the Customer Phone number: "))
Cust_vehicle=input(" |Enter the Customer vehicle: ")
Vehicle_No=input(" |Enter the Vehicle number: ")
service=input(" |Enter type of sevice: ")
Vehicle_part=input(" |Enter the name of parts installed: ")
price=int(input(" |Enter the Amount paid: "))
DateOfService=input(" |Enter the Date of service: ")
query="insert into CUSTOMER(Cust_ID,Cust_Name,Cust_Address,Phone_no,Cust_Vehicle,Vehicle_No,Service,Part_Used,Price,DateOfService)Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(Cust_id,Cust_name,Cust_address,Phone_no,Cust_vehicle,Vehicle_No,service,Vehicle_part,price,DateOfService)
cur.execute(query,val)
cn.commit()
print(" ")
print(" =======================================")
print(" | Inserted values |")
print(" =======================================")
x=input(" |Do you want to continue Y/N? ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
Customer()
elif ch==2:
update_cust()
elif ch==3:
delete()
elif ch==4:
view()
elif ch==5:
home()
else:
print(" |incorrect values|")
Customer()
def Inventory():
print(" =======================================")
print(" | Database Inventory |")
print(" =======================================")
print(" | |")
print(" | What do you wish to do? |")
print(" | 1.Add details of a new service |")
print(" | 2.Update details of an old service |")
print(" | 3.Delete records |")
print(" | 4.View records |")
print(" | 5.Return to homescreen |")
print(" =======================================")
ch=int(input(" |enter your choice:"))
if ch==1:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
Service_id=int(input(" |Enter the Service ID: "))
Service=input(" |Enter the Service name: ")
Part_used=input(" |Enter the Parts used:")
Quantity_left=int(input(" |Enter the Quantity left: "))
Monthly_earned=input(" |Enter the Monthly earnings: ")
Date_of_restock=input(" |Enter the Date of Restock: ")
sold=input(" |Enter the Quantity sold: ")
query="insert into INVENTORY(Service_ID,Service,Part_Used,Qty,Monthly_Earned,DateOfRestock,Quantity_Sold)Values(%s,%s,%s,%s,%s,%s,%s)"
val=(Service_id,Service,Part_used,Quantity_left,Monthly_earned,Date_of_restock,sold)
cur.execute(query,val)
cn.commit()
print(" ")
print(" =======================================")
print(" | Inserted values |")
print(" =======================================")
x=input(" |Do you want to continue Y/N? ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
Inventory()
elif ch==2:
update_inventory()
elif ch==3:
inventory_delete()
elif ch==4:
inventory_view()
elif ch==5:
home()
else:
print("incorrect values")
Inventory()
def update_cust():
while True:
print(" ")
print(" =======================================")
print(" | what do you wish to update? |")
print(" =======================================")
print(" | 1.single field |")
print(" | 2.multiple fields |")
print(" | 3.go back to previous menu |")
print(" =======================================")
x=int(input(" |Enter your choice:"))
if x==1:
print(" ")
print(" =======================================")
print(" | select field to be updated: |")
print(" =======================================")
print(" | 1.Customer name |")
print(" | 2.Customer Address |")
print(" | 3.phone number |")
print(" | 4.Customer Vehicle |")
print(" | 5.Vehicle Number |")
print(" | 6.Service |")
print(" | 7.Vehicle part |")
print(" | 8.Money paid |")
print(" | 9.Date of Service |")
print(" =======================================")
y=int(input(" |enter your choice: "))
if y==1:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database=" dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
print(" ")
Cust_id=int(input(" |enter the Customer's ID: "))
fn=input(" |Enter the New Name: ")
query="update Customer set Cust_Name=%s where Cust_ID=%s"
val=(fn,Cust_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_cust()
elif y==2:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
print(" =======================================")
Cust_id=int(input(" |enter the Customer's ID: "))
fn=input(" |Enter the New Address: ")
query="update Customer set Cust_Address=%s where Cust_ID=%s"
val=(fn,Cust_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_cust()
elif y==3:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
print(" =======================================")
Cust_id=int(input(" |enter the Customer's ID: "))
fn=int(input(" |Enter the New Phone number:"))
query="update Customer set Phone_no=%s where Cust_ID=%s"
val=(fn,Cust_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_cust()
elif y==4:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
print(" =======================================")
Cust_id=int(input(" |enter the Customer's ID: "))
fn=input(" |Enter the Vehicle name: ")
query="update Customer set Cust_Vehicle=%s where Cust_ID=%s"
val=(fn,Cust_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_cust()
elif y==5:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
print(" =======================================")
Cust_id=int(input(" |enter the Customer's ID:"))
fn=int(input(" |Enter the New Vehicle number:"))
query="update Customer set Vehicle_No=%s where Cust_ID=%s"
val=(fn,Cust_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_cust()
elif y==6:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
print(" =======================================")
Cust_id=int(input(" |enter the Customer's ID: "))
fn=input(" |Enter the Service:")
query="update Customer set Service=%s where Cust_ID=%s"
val=(fn,Cust_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_cust()
elif y==7:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
print(" =======================================")
Cust_id=int(input(" |enter the Customer's ID: "))
fn=input(" |Enter the Vehicle parts: ")
query="update Customer set Vehicle_Part=%s where Cust_ID=%s"
val=(fn,Cust_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_cust()
elif y==8:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
print(" =======================================")
Cust_id=int(input(" |enter the Customer's ID: "))
fn=int(input(" |Enter the New Amount paid: "))
query="update Customer set Price=%s where Cust_ID=%s"
val=(fn,Cust_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_cust()
elif y==9:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
print(" =======================================")
Cust_id=int(input(" |enter the Customer's ID: "))
fn=input(" |Enter the New Date of service: ")
query="update Customer set DateOfService=%s where Cust_ID=%s"
val=(fn,Cust_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_cust()
else:
print(" =======================================")
print(" | incorrect value |")
print(" =======================================")
update_cust()
elif x==2:
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
while True:
print(" =======================================")
Cust_id=int(input(" |enter the Customer's ID:"))
fn=input(" |Enter the New Name: ")
address=input(" |Enter the New Address: ")
phone=int(input(" |Enter the New Phone number: "))
vehicle=input(" |Enter the Vehicle name: ")
num=input(" |Enter the New Vehicle number: ")
service=input(" |Enter the Service: ")
parts=input(" |Enter the Vehicle parts: ")
paid=int(input(" |Enter the New Amount paid: "))
date=input(" |Enter the New Date of service: ")
query1="update Customer set Cust_Name=%s where Cust_ID=%s"
val1=(fn,Cust_id)
query2="update Customer set Cust_Address=%s where Cust_ID=%s"
val2=(address,Cust_id)
query3="update Customer set Phone_no=%s where Cust_ID=%s"
val3=(phone,Cust_id)
query4="update Customer set Cust_Vehicle=%s where Cust_ID=%s"
val4=(vehicle,Cust_id)
query5="update Customer set Vehicle_No=%s where Cust_ID=%s"
val5=(num,Cust_id)
query6="update Customer set Service=%s where Cust_ID=%s"
val6=(service,Cust_id)
query7="update Customer set Part_Used=%s where Cust_ID=%s"
val7=(parts,Cust_id)
query8="update Customer set Price=%s where Cust_ID=%s"
val8=(paid,Cust_id)
query9="update Customer set DateOfService=%s where Cust_ID=%s"
val9=(date,Cust_id)
cur.execute(query1,val1)
cur.execute(query2,val2)
cur.execute(query3,val3)
cur.execute(query4,val4)
cur.execute(query5,val5)
cur.execute(query6,val6)
cur.execute(query7,val7)
cur.execute(query8,val8)
cur.execute(query9,val9)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_cust()
elif x==3:
Customer()
else:
print(" =======================================")
print(" | incorrect value |")
print(" =======================================")
update_cust()
def update_inventory():
import mysql.connector as SQL
cn=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
if cn.is_connected():
cur=cn.cursor()
print(" ")
print(" =======================================")
print(" | what do you wish to update? |")
print(" =======================================")
print(" | 1.single field |")
print(" | 2.multiple fields |")
print(" | 3.go back to previous menu |")
print(" =======================================")
x=int(input(" |Enter your choice:"))
if x==1:
print(" ")
print(" =======================================")
print(" | select field to be updated: |")
print(" =======================================")
print(" | 1.Service |")
print(" | 2.Part Used |")
print(" | 3.Quantity Left |")
print(" | 4.Monthly Earned |")
print(" | 5.Date of Restock |")
print(" | 6.Quantity sold |")
print(" =======================================")
y=int(input(" |enter your choice: "))
if y==1:
while True:
Service_id=int(input(" |enter the Service ID:"))
fn=input(" |Enter the New Service:")
query="update INVENTORY set Service=%s where Service_ID=%s"
val=(fn,Service_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_inventory()
elif y==2:
while True:
Service_id=int(input(" |enter the Service ID:"))
fn=input(" |Enter the Part used:")
query="update INVENTORY set Part_Used=%s where Service_ID=%s"
val=(fn,Service_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_inventory()
elif y==3:
while True:
Service_id=int(input(" |Enter the Service ID:"))
fn=int(input(" |Enter the Quantity left:"))
query="update INVENTORY set Qty=%s where Service_ID=%s"
val=(fn,Service_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_inventory()
elif y==4:
while True:
Service_id=int(input(" |Enter the Service ID:"))
fn=int(input(" |Enter Monthly earnings:"))
query="update INVENTORY set Monthly_Earned=%s where Service_ID=%s"
val=(fn,Service_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_inventory()
elif y==5:
while True:
Service_id=int(input(" |Enter the Service ID:"))
fn=input(" |Enter the Date of restock:")
query="update INVENTORY set DateOfRestock=%s where Service_ID=%s"
val=(fn,Service_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_inventory()
elif y==6:
while True:
Service_id=int(input(" |Enter the Service ID:"))
fn=int(input(" |Enter the Quantity sold:"))
query="update INVENTORY set Quantity_Sold=%s where Service_ID=%s"
val=(fn,)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_inventory()
else:
print(" =======================================")
print(" | incorrect value |")
print(" =======================================")
cn.close()
update_inventory()
elif x==2:
while True:
print(" =======================================")
Service_id=int(input(" |Enter the Service ID:"))
Service=input(" |Enter the New Service:")
Part_Used=input(" |Enter the Part Used:")
Qty=int(input(" |Enter the Quantity left:"))
Monthly_Earned=int(input(" |Enter Monthly earnings:"))
DateOfRestock=input(" |Enter the Date of restock:")
Quantity_Sold=int(input(" |Enter the Quantity sold:"))
query="update INVENTORY set Service=%s,Part_Used=%s,Qty=%s,Monthly_Earned=%s,DateOfRestock=%s,Quantity_Sold=%s where Service_ID=%s"
val=(Service,Part_Used,Qty,Monthly_Earned,DateOfRestock,Quantity_Sold,Service_id)
cur.execute(query,val)
print(" ")
print(" =======================================")
print(" | updated values |")
print(" =======================================")
cn.commit()
x=input(" |Do you want to continue Y/N ")
print(" ")
if x=="N" or x=="n":
break
cn.close()
update_inventory()
elif x==3:
cn.close()
Inventory()
else:
print(" =======================================")
print(" | incorrect value |")
print(" =======================================")
cn.close()
update_inventory()
def delete():
print(" =======================================")
print(" | what do you wish to do? |")
print(" =======================================")
print(" | 1. Delete a field |")
print(" | 2.go back to previous menu |")
print(" =======================================")
x=int(input(" |Enter your choice:"))
if x == 1:
import mysql.connector as SQL
con=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
cursor=con.cursor()
code=int(input(" |Enter Customer ID to Delete:"))
query="delete from Customer where Cust_ID={}".format(code)
cursor.execute(query)
con.commit()
if cursor.rowcount>0:
print(" =======================================")
print(" | Deletion Successfull.. |")
print(" =======================================")
y=input(" |do you want to continue Y/N: ")
print(" ")
if y=="Y":
delete()
else:
Customer()
else:
print(" =======================================")
print(" | Customer ID not Found |")
print(" =======================================")
print(" ")
delete()
if x == 2:
print(" ")
Customer()
def view():
print(" ")
print(" =======================================")
print(" | what do you wish to view? |")
print(" =======================================")
print(" | 1.single record |")
print(" | 2.all records |")
print(" | 3.go back to previous menu |")
print(" =======================================")
x=int(input(" |Enter your choice:"))
if x == 1:
import mysql.connector as SQL
con=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
cursor=con.cursor()
t=int(input(" |enter customer ID to view: "))
print(" ")
query="select * from Customer where Cust_ID={}".format(t)
cursor.execute(query)
data=cursor.fetchone()
print(data)
print(" ")
print(" =======================================")
y=input(" |do you want to continue Y/N: ")
print(" =======================================")
print(" ")
if y=="Y":
view()
else:
Customer()
if x == 2:
print(" ")
import mysql.connector as SQL
con=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
cursor=con.cursor()
cursor.execute("select * from Customer")
record=cursor.fetchall()
print("{:^10}".format(""))
print("="*190)
print("{:^8}{:^20}{:^23}{:^15}{:^17}{:^17}{:^17}{:^18}{:^10}{:^10}".format("Cust_ID","Cust_Name","Cust_Address","Phone_no","Cust_Vehicle","Vehicle_No","Service","Part_Used","Price","DateOfService"))
print("="*190)
for i in record:
x,y,z,d,e,f,v,w,u,t=i
print("{:^8}{:^20}{:^23}{:^15}{:^17}{:^17}{:^17}{:^18}{:^10}{:^10}".format(x,y,z,d,e,f,v,w,u,t))
print("="*190)
print("Total Number of records=",cursor.rowcount)
print(" ")
print(" ")
print(" =======================================")
y=input(" |do you want to continue Y/N: ")
print(" =======================================")
print(" ")
if y=="Y":
view()
else:
Customer()
if x == 3:
Customer()
def inventory_view():
print(" ")
print(" =======================================")
print(" | what do you wish to view? |")
print(" =======================================")
print(" | 1.single record |")
print(" | 2.all records |")
print(" | 3.go back to previous menu |")
print(" =======================================")
x=int(input(" |Enter your choice:"))
if x == 1:
import mysql.connector as SQL
con=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
cursor=con.cursor()
t=int(input(" |Enter service ID to view: "))
query="select * from INVENTORY where Service_ID={}".format(t)
cursor.execute(query)
data=cursor.fetchone()
print(data)
print(" ")
print(" =======================================")
y=input(" |do you want to continue Y/N: ")
print(" =======================================")
print(" ")
if y=="Y":
inventory_view()
else:
Inventory()
if x == 2:
import mysql.connector as SQL
con=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
cursor=con.cursor()
cursor.execute("select * from INVENTORY")
record=cursor.fetchall()
print("{:^10}".format(""))
print("="*150)
print("{:^20}{:^30}{:^20}{:^15}{:^15}{:^15}{:^15}".format("Service_ID","Service","Part_Used","Qty","Monthly_Earned","DateOfRestock","Quantity_Sold"))
print("="*150)
for i in record:
x,y,z,d,e,f,v=i
print("{:^20}{:^30}{:^20}{:^15}{:^15}{:^15}{:^15}".format(x,y,z,d,e,f,v))
print("="*150)
print("Total Number of records=",cursor.rowcount)
print(" ")
print(" =======================================")
y=input(" |do you want to continue Y/N: ")
print(" =======================================")
print(" ")
if y=="Y":
inventory_view()
else:
Inventory()
if x == 3:
Inventory()
def inventory_delete():
print(" =======================================")
print(" | what do you wish to do? |")
print(" =======================================")
print(" | 1. Delete a field |")
print(" | 2.go back to previous menu |")
print(" =======================================")
x=int(input(" |Enter your choice:"))
if x == 1:
import mysql.connector as SQL
con=SQL.connect(host="localhost",user="root",passwd="",database="dga_garages")
cursor=con.cursor()
code=int(input(" |Enter Service ID to Delete:"))
query="delete from INVENTORY where Service_ID={}".format(code)
cursor.execute(query)
con.commit()
if cursor.rowcount>0:
print(" =======================================")
print(" | Deletion Successfull.. |")
print(" =======================================")
y=input(" |do you want to continue Y/N: ")
print(" ")
if y=="Y":
inventory_delete()
else:
Inventory()
else:
print(" =======================================")
print(" | Customer ID not Found |")
print(" =======================================")
print(" ")
inventory_delete()
if x == 2:
Inventory()
login()
