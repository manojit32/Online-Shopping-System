import pickle
import sys
import os
import datetime
import matplotlib.pyplot as plt
from Admin import *

class Cart:
	def __init__(self,products,total):
		self.products=products
		self.total=total

	def add(self,id):
		llist=Admin.ViewProducts()
		prod=self.products
		x=self.total
		for j in llist:
			for i in j.keys():
				if i=='id' and j[i]==id:
					prod.append(j)
					x+=int(j['price'])
					break
		self.products=prod
		self.total=x

	def view(self):
		for i in self.products:	
			print(i['name']+" "+i['price']+" "+i['id'])

	def delete(self, id):
		f=0
		for i in self.products:
			for k in i.keys():
				if k=="id" and i[k]==id:
					self.products.remove(i)
					self.total-=int(i["price"])
					f=1
					break
		if f==0:
			print("Item Not Here")