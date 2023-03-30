from tabulate import tabulate
import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='', database='clientdb')

if conn.is_connected():
	print("Connection established..")
"""
def insert(name, age, address, tel):
	res=conn.cursor()
	sql = "insert into client (name, age, address, tel) values (%s, %s, %s, %s)"
	user = (name, age, address, tel)
	res.execute(sql, user)
	conn.commit()
	print("records well inserted!!")

def update(name, age, address, tel, id):
	res = conn.cursor()
	sql = "update client set name = %s, age = %s, address = %s, tel = %s where id = %s"
	user = (name, age, address, tel, id)
	res.execute(sql, user)
	conn.commit()
	print("record is well updated")

def select():
	res = conn.cursor()
	sql = "select * from client"
	res.execute(sql)
	result = res.fetchall()
	print(tabulate(result, headers=["ID","NAME","AGE","ADDRESS","TELEPHONE"]))

def delete(id):
	res = conn.cursor()
	sql = "delete from client where id=%s"
	user = (id,)
	res.execute(sql, user)
	conn.commit()
	print("Record is deleted successfully")

while True:
	print("1. Insert Data")
	print("2. Update data")
	print("3. Select Data")
	print("4. Delete Data")
	print("5. Exit")
	
	choice = int(input("Enter your Choice: "))

	if choice == 1:
		name = input("Enter Name: ")
		age = input("Enter Age: ")
		address = input("Enter the address: ")
		tel = input("Enter the telephone: ")

		insert(name, age, address, tel)

	elif choice == 2:
		id = input("Enter the ID: ")
		name = input("Enter Name: ")
		age = input("Enter Age: ")
		address = input("Enter the address: ")
		tel = input("Enter the telephone: ")
		
		update(name, age, address, tel, id)
	
	elif choice == 3:
		select()

	elif choice == 4:
		id = input("Enter the id of record to be deleted: ")
		delete(id)
	
	elif choice == 5:
		quit()
	
	else:
		print("Invalid input, try again!")
"""