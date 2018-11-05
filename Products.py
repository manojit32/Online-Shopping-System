import pickle
import sys
import os
import datetime
import matplotlib.pyplot as plt

class Products:
	def __init__(self,id,name,group,subgroup,price):
		self.id=id
		self.name=name
		self.group=group
		self.subgroup=subgroup
		self.price=price
		
	def storeProducts(self):
		d={"id":self.id,"name":self.name,"group":self.group,"subgroup":self.subgroup,"price":self.price}
		file=open('products','ab')
		pickle.dump(d,file)
		file.close()
