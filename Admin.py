import pickle
import sys
import os
import datetime
import matplotlib.pyplot as plt
from Products import *

class Admin:
	def __init__(self,id,name):
		self.id = id
		self.name = name
	@staticmethod
	def ViewProducts():
	    try:
		    file = open('products','rb')
		    llist=[]
		    while True:
			    try:
			        llist.append(pickle.load(file))
			    except EOFError:
			        break
		    file.close()
		    return llist
	    except IOError:
	        print("No products found")

	def AddProducts(self, id, name, group, subgroup, price):
		product=Products(id, name, group, subgroup, price)
		file=open('products','rb')
		llist=[]
		while True:
			try:
				llist.append(pickle.load(file))
			except EOFError:
				break
		f=0
		for j in llist:
			for i in j.keys():
				if i=='id' and j[i]==id:
					f=1
					break
		if f==1:
			print("ID Not available")
			id1=input("Id: ")
			name1=input("Name: ")
			gr1=input("Group: ")
			sgr1=input("Subgroup: ")
			pr1=input("Price: ")
			self.AddProducts(id1,name1,gr1,sgr1,pr1)
		else:
			product.storeProducts()
		file.close()
		

	def DeleteProducts(self,id):
		llist=self.ViewProducts()
		for j in llist:
			for i in j.keys():
				if i=='id' and j[i]==id:
					llist.remove(j)
					break
		file=open('products','wb')
		for i in llist:
			pickle.dump(i,file)
		file.close()

	def ModifyProducts(self,id, name='', group='',subgroup='',price=''):
		llist=self.ViewProducts()
		for j in llist:
			for i in j.keys():
				if i=='id' and j[i]==id:
					if name!='':
						j['name']=name
					if group!='':
						j['group']=group
					if subgroup!='':
						j['subgroup']=subgroup
					if price!='':
						j['price']=price
					break
		file=open('products','wb')
		for i in llist:
			pickle.dump(i,file)
		file.close()

	def MakeShipment(self):
		try:
			f=open('shopping_history','rb')
			llist=[]
			while True:
				try:
					llist.append(pickle.load(f))
				except EOFError:
					break
			f.close()
			for i in llist:
				for j in i:
					if "status" in j.keys():
						j["status"]="shipped"
			f=open('shopping_history','wb')
			for i in llist:
				print(i)
				pickle.dump(i,f)
		except IOError:
			print("No shopping history")

	def shopping_history(self):
		try:
			f=open('shopping_history','rb')
			llist=[]
			while True:
				try:
					llist.append(pickle.load(f))
				except EOFError:
					break
			f.close()
			for i in llist:
				print(i)
		except IOError:
			print("No Shopping History found !!")

	def ViewGraph(self):
		try:
			f=open('shopping_history','rb')
			llist=[]
			while True:
				try:
					llist.append(pickle.load(f))
				except EOFError:
					break
			f.close()
			count=0
			f1=open('customer','rb')
			while True:
				try:
					d=pickle.load(f1)
					count+=1
				except EOFError:
					break
			f1.close()
			#print(count)
			fig1=plt.figure()
			color=['y','b','g','r']
			for i in range(1,count+1):
				time=[]
				bill=[]
				for k in llist:
					for j in k:
						if 'user_id' in j.keys():
							#print(j)
							if j['user_id']==str(i):
								#print(j)
								time.append(j["timestamp"][11:19])
								bill.append(j["Bill"])
				#print(time)
				#print(bill)
				#print("\n")
				ax1=fig1.add_subplot(count,1,i)
				ax1.plot(time,bill,'o-',color=color[i],label='User '+str(i))
				ax1.legend(loc='best')
				ax1.set_ylim([0,max(bill)+10])
				ax1.set_xlabel("Timestamp")
				ax1.set_ylabel("Bill")
			plt.show()
							
		except IOError:
			print("No Shopping History found !!")