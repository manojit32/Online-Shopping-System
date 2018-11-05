import pickle
import sys
import os
import datetime
import matplotlib.pyplot as plt
from Guest import *
from Customer import *
from Products import *
from Admin import *
from Cart import *
from Payment import *


def admin_menu(admin_id):
	f=0
	file=open('admin','rb')
	while True:
		try:
			d=pickle.load(file)
			if d['id']==admin_id:
				f=1
				name=d['name']
				break
		except EOFError:
			break
	file.close()
	if f==1:
		admin=Admin(admin_id,name)
		print("1.View Products")
		print("2.Add Product")
		print("3.Delete Product")
		print("4.Modify Product")
		print("5.View Order History")
		print("6.Make Shipment")
		print("7.View Purchase Graph")
		print("8.Logout")
		inp=input("Enter choice : ")
		if inp=="1":
			llist=admin.ViewProducts()
			for i in llist:
				print(i)
			print("\n")
			admin_menu(admin_id)
		if inp=='2':
			id=input("Product Id: ")
			name=input("Product Name: ")
			gr=input("Product Group: ")
			sgr=input("Product subgroup: ")
			pr=input("Product Price: ")
			admin.AddProducts(id,name,gr,sgr,pr)
			print("\n")
			admin_menu(admin_id)

		if inp=='3':
			id=input("Product Id : ")
			admin.DeleteProducts(id)
			print("\n")
			admin_menu(admin_id)

		if inp=='4':
			id=input("Product Id: ")
			name=input("Product Name: ")
			gr=input("Product Group: ")
			sgr=input("Product subgroup: ")
			pr=input("Product Price: ")
			admin.ModifyProducts(id,name,gr,sgr,pr)
			print("\n")
			admin_menu(admin_id)
		if inp=='5':
			admin.shopping_history()
			print("\n")
			admin_menu(admin_id)
		if inp=='6':
			admin.MakeShipment()
			print("\n")
			admin_menu(admin_id)
		if inp=='7':
			admin.ViewGraph()
			print("\n")
			admin_menu(admin_id)

		if inp=='8':
			print("\n")
			main()
			return
	else:
		print("Wrong ID given")
		admin_id=input("Give Admin id or Press A for Menu: ")
		if admin_id=='A':
		    main()
		else:
		    admin_menu(admin_id)
	

def admin_reg(admin_id,name):
	f=0
	file=open('admin','rb')
	while True:
		try:
			d=pickle.load(file)
			if d['id']==admin_id:
				f=1
				break
		except EOFError:
			break
	file.close()
	if f==0:
		t={"id":admin_id,"name":name}
		file=open('admin','ab')
		pickle.dump(t,file)
		file.close()
	else:
		print("Admin ID Already exists!")
		id1=input("User id: ")
		name1=input("Name: ")
		admin_reg(id1,name1)
	admin_menu(admin_id)

def customer_menu(name,c):
	print("1.View Products")
	print("2.Add To Cart")
	print("3.View Cart")
	print("4.Delete From Cart")
	print("5.Make Payment")
	print("6.Logout")
	inp=input("Enter choice : ")
	if inp=="1":
		llist=Admin.ViewProducts()
		for i in llist:
			print(i)
		print("\n")
		customer_menu(name,c)
	if inp=="2":
		admin_id=input("Product Id: ")
		c.AddToCart(admin_id)
		print("\n")
		customer_menu(name,c)
	if inp=='3':
		c.ViewCart()
		print("\n")
		customer_menu(name,c)
	if inp=='4':
		id=input("Product Id: ")
		c.DeleteFromCart(id)
		print("\n")
		customer_menu(name,c)
	if inp=="5":
		c.makePayment()
		print("\n")
		customer_menu(name,c)
	if inp=="6":
		main()



def customer_login(admin_id):
	f=0
	name=''
	file=open('customer','rb')
	while True:
		try:
			d=pickle.load(file)
			if d['id']==admin_id:
				f=1
				name=d['name']
				llist=[]
				cart1=Cart(llist,0)
				payment=Payment()
				c=Customer(admin_id,name,d['address'],d['phone'],cart1,payment)
				break
		except EOFError:
			break
	file.close()
	if f==1:
		customer_menu(name,c)

	else:
		print("Wrong ID")
		admin_id=input("Give User id or Press A for Menu: ")
		if admin_id=='A':
		    main()
		else:
		    customer_login(admin_id)

def guest_reg(admin_id,name,address,ph,cart1,payment):
	f=0
	file=open('customer','rb')
	while True:
		try:
			d=pickle.load(file)
			if d['id']==admin_id:
				f=1
				break
		except EOFError:
			break
	file.close()
	if f==0:
		c=Customer(admin_id,name,address,ph,cart1,payment)
		c.store_cust()
	else:
		id1=input("User Id: ")
		name1=input("Name: ")
		address1=input("Address: ")
		ph1=input("Phone No.: ")
		car1=Cart([],0)
		pay1=Payment()
		guest_reg(id1,name1,address1,ph1,car1,pay1)
	customer_login(admin_id)




def main():
	print("Welcome to Online Shopping Store")
	print("Enter your choice")
	print("1.Admin")
	print('2.Customer')
	print('3.Guest')
	print('4.Exit')
	inp=int(input("Enter your choice : "))
	if inp==1:
		print("Choose an option: ")
		print("1.Register")
		print("2.Login")
		y=int(input("Enter Choice : "))
		if y==1:
			admin_id=input("User id: ")
			name=input("Name: ")
			admin_reg(admin_id,name)
		if y==2:
			admin_id=input("User id: ")
			admin_menu(admin_id)
	if inp==2:
		print("Choose an option: ")
		print("1.Login")
		print("2.Exit")
		y=int(input())
		if y==1:
			admin_id=input("User id: ")
			customer_login(admin_id)
		if y==2:
			print("Thanks for shopping !!")
			sys.exit()

	if inp==3:
		print("1.Register")
		print("2.View Products")
		print("3.Exit")
		y=int(input())
		if y==1:
			id=input("User Id: ")
			name=input("Name: ")
			addr=input("Address: ")
			phno=input("Phone No.: ")
			mycart=Cart([],0)
			payment=Payment()
			guest_reg(id,name,addr,phno,mycart,payment)
		if y==2:
			Guest.ViewProducts()
			print("\n")
			main()
		if y==3:
			print("Thanks for Shopping !!")
			sys.exit()

	if inp==4:
		print("Thanks for shopping!")
		sys.exit()

if __name__=='__main__':
	l={}
	try:
		file=open("admin","rb")
		file.close()
	except IOError:
		file=open("admin","wb")
		pickle.dump(file,l)
		file.close()
	l={}
	try:
		file1=open("customer","rb")
		file1.close()
	except IOError:
		file1=open("customer","wb")
		pickle.dump(file1,l)
		file1.close()
	main()
	