from threading import Thread
from time import sleep
''' method 1
class one (Thread):
  def run (self):
    print ("started" )
    for i in range (5):
      print ("downloading[1]...")
      sleep(1)
    print ("done..")


class two (Thread):
  def run (self):
    print ("started" )
    for i in range (5):
      print ("downloading[2]...")
      sleep(1)
    print ("done..")


call1 = one()
call2 = two()
call1.start()
call2.start()
''' 
# Python program to illustrate the concept
# of threading
# importing the threading module

import threading
def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))
    sleep(1)
    print ("done{1}..")
 
def print_square(num):
    # function to print square of given num
    print("Square: {}" .format(num * num))
    sleep(1)
    print ("done{2}..")

def print_somthing(num):
    # function to print square of given num
    print("Square: {}" .format(num * num/num+num-num))
    sleep(1)
    print ("done{3}..") 
 

if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10, ))
    t2 = threading.Thread(target=print_cube, args=(20,))
    t3 = threading.Thread(target=print_somthing,args=(30,))
     # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # wait until thread 2 is completely executed
    t3.join()
    # both threads completely executed
    print("Done!")