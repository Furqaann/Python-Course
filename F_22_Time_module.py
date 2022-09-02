"""
 Author: Furqan Fiaz
 Date: 21-08-2022, 6.31 Pm
 This file will contain the information about Time module in Python
"""
import time
# what if we want to find the time complexity of the desired function we use time module
a=0
initial_time=time.time()
while(a<200):
    print("You're Awesome")
    a+=1
print("The time complecity of for loop",time.time()-initial_time)
for i in range(10):
    print("Hello!You're Awesome")
print("The time complecity of for loop",initial_time-time.time())

current_time=time.asctime()
print(current_time)