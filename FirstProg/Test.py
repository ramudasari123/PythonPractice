for i in range (2,10,2):
    print(i)

j=0
while(j<=4):
    print("j is ",j)
    j=j+1
k=1
for k in range(1,7):
    print("k is ",k)
    if(k>1):
        print("k is greater than 1")
    else:
        print("k is smaller than 1")
    k=k+1
else:
    print("k is greater")
    k=k+1

def addition(n1,n2,s1):
    n3=n1+n2
    s2=s1.upper()
    print("addition is ",n3)
    print("upper case value is ",s2)

addition(3,8,"raM")

names = ["ram","goud","prabha","ntr",2,6]
print(names)
print(names[2:4])
print(names.remove("goud"))
print(names)

a = "rams"
print(a.upper())
print(len(a))