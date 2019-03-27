import os
import time

#Write Data to a file
file=open('D:\TRAININGS\Python\python_workspace/test.txt','w')
file.write("hi, wt r u dng")
file.close()

#Read Data from a file
file=open("D:\TRAININGS\Python\python_workspace/test.txt","r")
print(file.read())
file.close()

#rename a file
os.rename("D:\TRAININGS\Python\python_workspace/test.txt","D:\TRAININGS\Python\python_workspace/test1.txt")
os.rename("D:\TRAININGS\Python\python_workspace/test1.txt","D:\TRAININGS\Python\python_workspace/test.txt")

#work on a folder
os.mkdir("ram")
print(os.getcwd())
time.sleep(2)
os.rmdir("ram")


