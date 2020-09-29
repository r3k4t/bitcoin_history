
import os
import sys
import time
os.system("clear")
time.sleep(1)
print ("   ############## Author : Rahat Khan Tusar(RKT) #############")
time.sleep(2)
print ("################ Github : https://github.com/r3k4t ################ ")
time.sleep(3)
print
import bitcoin
from bitcoin import *
a_valid_bitcoin_address = raw_input("Enter a valid bitcoin address :")
print (history(a_valid_bitcoin_address))
