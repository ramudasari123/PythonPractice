file1=open("D:/TRAININGS/Python/python_workspace/Practice/Data/sampletext.txt",mode='w')
#print(file1.read())
#file1.seek(0)
#print(file1.read())
file1.write("wt r u dng")
file1.close()
file1=open("D:/TRAININGS/Python/python_workspace/Practice/Data/sampletext.txt",mode='r')
print(file1.read())

with open("D:/TRAININGS/Python/python_workspace/Practice/Data/sampletext.txt") as f:
    print(f.read())
with open("D:/TRAININGS/Python/python_workspace/Practice/Data/sampletext.txt",mode='a') as d:
    d.write("\noyy")

with open("D:/TRAININGS/Python/python_workspace/Practice/Data/sampletext.txt",mode='r') as f:
    print(f.read())