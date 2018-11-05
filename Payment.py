import pickle
import sys
import os
import datetime
import matplotlib.pyplot as plt

class Payment():
	def CreateBill(self, cart):
		for i in cart.products:
			print(i['name']+" "+i['price'])
		print("Total Bill: ",str(cart.total))
		return cart.total