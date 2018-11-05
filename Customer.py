import pickle
import sys
import os
import datetime
import matplotlib.pyplot as plt
from Cart import *

class Customer:
	def __init__(self,id,name,address,phone,cart,payment):
		self.id=id
		self.name=name
		self.address=address
		self.phone=phone
		self.cart=cart
		self.payment=payment

	def store_cust(self):
		d={'id':self.id,'name':self.name,'address':self.address, 'phone':self.phone}
		file=open('customer','ab')
		pickle.dump(d,file)
		file.close()

	def AddToCart(self,id):
		self.cart.add(id)
		
	def ViewCart(self):
		self.cart.view()

	def DeleteFromCart(self,id):
		self.cart.delete(id)

	def makePayment(self):
		bill=self.payment.CreateBill(self.cart)
		file=open('shopping_history','ab')
		new=[{"user_id":self.id,"timestamp":str(datetime.datetime.now()),"status":"confirmed","Bill":bill}]
		if self.cart.products!=[]:
			pickle.dump(new+self.cart.products,file)
		self.cart=Cart([],0)
		file.close()