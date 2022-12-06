import numpy as np
import time

#preparar data
np.random.RandomState(100)
arr=np.random.randint(0,10,size=[200000,5])
data=arr.tolist()
data[:5]

'''
python has a module named time, to handrle time-related task

'''

#python time.ptime()
'''
this function returns seconds since a reference date
tipicale this date is epoch=January 1, 1970, 00:00:00 at UTC
'''
seconds=time.time()
print("seconds since epoch=",seconds)

'''
local_time
return string representing local time
'''
local_time=time.ctime(seconds)
print("Local time since epoch",local_time)

'''
time.sleep(seconds)
we can make python wait seconds before print or 
do some accion
'''
print("0 seconds has passed")
time.sleep(3)
print("3 seconds has passed")
time.sleep(2)
print("2 more seconds has passed")
