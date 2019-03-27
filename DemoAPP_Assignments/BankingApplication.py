from tkinter import *

Mwindow1=Tk()
Mwindow1.title('Info Bnak')
Mwindow1.geometry('500x500')

customerDict={'cust1':1}
balance=0
custName=''
names=StringVar()
mony=IntVar()

def createCustomer():
    custCreationWin=Tk()
    custCreationWin.title('Welcome To Info Bank Customer Creation')
    custCreationWin.geometry('250x250')
    namelab=Label(custCreationWin,text='Customer Name',bg='white',font=3).grid(row=3,column=1)
    name=Entry(custCreationWin,textvariable=names,font=3).grid(row=3,column=2)
    monDep = Label(custCreationWin,text='Amount', bg='white', font=3).grid(row=4, column=1)
    depamount=Entry(custCreationWin,textvariable=mony,font=3).grid(row=4, column=2)
    createbtn=Button(custCreationWin,text='Create',font=3,bg='white',command=addCustomer(names.get(),mony.get())).grid(row=5, column=2)
    quitbtn=Button(custCreationWin,text='Quit',font=3,bg='white',command=custCreationWin.quit).grid(row=6,column=2)

def depositMoney():
    WdepositMoney=Tk()
    WdepositMoney.title('Welcome to Info Bank Deposit')
    WdepositMoney.geometry('250x250')
    namelab = Label(WdepositMoney,text='Customer Name', bg='white', font=3).grid(row=3, column=1)
    name = Entry(WdepositMoney, textvariable=names, font=3).grid(row=3, column=2)
    monDep = Label(WdepositMoney,text='Amount', bg='white', font=3).grid(row=4, column=1)
    depamount = Entry(WdepositMoney, textvariable=mony, font=3).grid(row=4, column=2)
    depbtn=Button(WdepositMoney,text='Deposit',font=3,bg='white',command=deposit(names.get(), mony.get())).grid(row=5,column=2)
    quitbtn=Button(WdepositMoney,text='Quit',font=3,bg='white',command=WdepositMoney.quit).grid(row=6,column=2)

def withdrwaMoney():
    Wwithdrawmn=Tk()
    Wwithdrawmn.title('Welcome to Info Bank Money WithDraw')
    Wwithdrawmn.geometry('250x250')
    namelab = Label(Wwithdrawmn, text='Customer Name', bg='white', font=3).grid(row=3, column=1)
    name = Entry(Wwithdrawmn, textvariable=names, font=3).grid(row=3, column=2)
    monDep = Label(Wwithdrawmn, text='Amount', bg='white', font=3).grid(row=4, column=1)
    depamount = Entry(Wwithdrawmn, textvariable=mony, font=3).grid(row=4, column=2)
    depbtn=Button(Wwithdrawmn,text='Deposit',font=3,bg='white',command=Withdrawl(names.get(), mony.get())).grid(row=5,column=2)
    qtnbtn=Button(Wwithdrawmn,text='Quit',font=3,bg='white',command=Wwithdrawmn.quit).grid(row=6,column=2)



def addCustomer(name,amount):
    money=balance+amount
    custName=name
    customerDict.update({custName:money})
    for nam,mon in customerDict.items():
        if(nam.upper()==custName.upper() and mon==money):
            Label(text='Welcome to our family, You Have successfuly created Account')
        else:
            Label(text='Sorry, Try Again Later')

def deposit(name,amount):
    for nam,val in customerDict.items():
        if(name.upper()==nam.upper()):
            val=val+amount

def Withdrawl(name,amount):
    for nam,val in customerDict.items():
        if(nam.upper()==name.upper() and val>amount+10):
            val=val-amount


moneydep=IntVar()
custName=StringVar()

'''
def deposit():
    Depositwindow=Tk()
    Depositwindow.title('Welcome to Deposit Section')
    Name=Entry(textvariable=custName,)
    depmoney1=Entry(Mwindow1,textvariable=moneydep,font=3).grid(row=7,column=2)
'''

label1=Label(Mwindow1,text='Welcome To Info Bank',bg='yellow').grid(row=1,column=6)
newJoin=Button(Mwindow1,text='NewCustomer',font=3,bg='blue',command=createCustomer).grid(row=3,Column=1)
buttondeposit=Button(Mwindow1,text='Deposit',bg='white',font=3,command=depositMoney).grid(row=4,column=1)
buttonwithdraw=Button(Mwindow1,text='Withdraw',bg='white',font=3,command=withdrwaMoney).grid(row=5,column=1)

Mwindow1.mainloop()