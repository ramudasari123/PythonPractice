def lettercap(text):
    let1=text[0].upper()
    let=text[3].upper()
    fulltext=let1+text[1:3]+let+text[4:]
    print("data modified is ",fulltext)

lettercap("ramanjaneyulu")

def reverseword(text,strings):
    letlist=text.split()
    wordrev=letlist[::-1]
    letter=strings[::-1]
    print("word list rev is ",wordrev)
    print("letter rev is ",letter)

reverseword("too many tasks",'strikes')

def comparisonnum(num):
    for i in range(0,len(num)-1):
        if num[i]==num[i+1]:
            return True
        else:
            return False
val=comparisonnum([1,3,5,5,6])
print('boolean condition is',val)

def PrimeList(num):
    listprime=[]
    nums=1
    while nums<=num:
        if nums%2==0:
            listprime.append(nums)
        nums+=1
    return listprime

pmlist=PrimeList(100)
print(pmlist)