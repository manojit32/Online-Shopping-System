import pickle
import sys
import os
import datetime
import matplotlib.pyplot as plt

class Guest:
    @staticmethod
    def ViewProducts():
        try:
            f = open('products','rb')
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
            print("No Products found !!")