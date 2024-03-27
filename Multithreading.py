#Implementing multithreading
#We will first import both threading and time
import threading
import time

#function was created that calculates the square of number
def longSquare(num): #pass in a number
    time.sleep(1) #pause for 1 second
    return num**2 #thus returning that number squared

[longSquare(n) for n in range(0,5)]
