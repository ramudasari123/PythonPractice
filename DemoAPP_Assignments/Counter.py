from tkinter import *

count=0
def conuter():
    value=a.get()
    for count in range (1,value):
        count =count+1
        Label(text=count,font=5).pack()


#num=input("Enetr counter number :")
root1=Tk()
a=IntVar()
root1.title("Welcome to Counter")
root1.geometry('500x500')
Label(root1,text='Hi user',fg='blue',font=5).pack()
Button(root1,text="clickMe",fg='green',bg='white',font=4,command=root1.destroy).pack()
inputbox=Entry(root1,textvariable=a).pack()
button2=Button(root1,text='Start',fg='green',bg='white',command=conuter).pack()
button3=Button(root1,text='close',fg='green',bg='white',command=root1.quit).pack()

#value1=float(int(value))

root1.mainloop()