 
import threading
import time

'''
this is a liena rprocess:
firs we will print a message after waiting 5 seconds
second we will print a mesage after waiting 5 more seconds
'''

'''
print("0 seconds has passed")
time.sleep(5)
print("5 seconds has passed")
time.sleep(5)
print("5 more seconds has passed")
#'''


'''
we can make 2 paralell process, this way if we need 
to wat a few seconds at each proccess, this will be waited in the 
same moment
'''

def wait_seconds_to_print(seconds):
    time.sleep(seconds)
    print(f'{seconds} has passed')

#wait_seconds_to_print(3)

def t1(seconds):
    wait_seconds_to_print(seconds)
#t1(3)
#print("testeo t1")    
def t2(seconds):
    wait_seconds_to_print(seconds)

#t2(3)
#print("testeo t2")  
    
proces1=threading.Thread(target=t1, args=[5.5])  #this object must be iterable[]
proceso=threading.Thread(target=t2,args=[5])

proces1.start()
proceso.start()
proces1.join() # this line of code is for wait before running the next lines of codes
proceso.join()
#waiting this 2 thread to finish
#
print("proceso finalizado")
