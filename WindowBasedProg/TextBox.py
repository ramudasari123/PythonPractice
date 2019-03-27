from tkinter import *

inputs=Tk()
inputs.title('Enter below Data')
inputs.geometry('500x500')

def ClearData():
    a1.delete(0,END)
    a2.delete(0,END)
    a3.delete(0, END)
    a4.delete(0, END)

Label(text='Fname').grid(row=0)
a1=Entry(inputs)
a1.grid(row=0,column=1)
a1.insert(0,'Ram')
Label(text='Lname').grid(row=1)
a2=Entry(inputs)
a2.grid(row=1,column=1)
a2.insert(0,'Dasari')
Label(text='eMail').grid(row=2)
a3=Entry(inputs)
a3.grid(row=2,column=1)
a3.insert(0,'demo@gmail.com')
Label(text='Phone').grid(row=3)
a4=Entry(inputs)
a4.grid(row=3,column=1)
a4.insert(0,'9876543210')

Button(text='clearAll',command=ClearData).grid(row=4,column=3)

inputs.mainloop()