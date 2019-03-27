import time
import calendar

print(time.time())
print(time.localtime(1545539715.996567))
print(time.process_time())
print(time.asctime())

for i in range(1,11):
    #input()
    for k in range(1,11):
        print(i,"*",k," =",i*k)
    #time.sleep(2)
    print("\n")

print("hi ram")
time.sleep(2)
print("hi DOG")

print(calendar.isleap(2009))
print(calendar.month(2018,10))
print(calendar.day_name(2019))