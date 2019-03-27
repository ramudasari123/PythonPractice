from tkinter import *

convr = Tk()
convr.geometry('500x500')
convr.title('Litres-Gallon Converter')
#Label(text='Welcome to Litres-Gallon Converter')

def calcator():
    litres=Value1.get()
    gallons=litres*0.264
    e2.insert(0,gallons)
def clr():
    e1.delete(0,END)
    e2.delete(0,END)

Value1=IntVar()

Label(text='Litres',font=3).grid(row=0,column=0)
e1=Entry(convr,textvariable=Value1)
e1.grid(row=0,column=1)
Label(text='Gallons',font=3).grid(row=1,column=0)
e2=Entry(convr)
e2.grid(row=1,column=1)
Button(text='Calculate',command=calcator,font=3).grid(row=2,column=1)
Button(text='Clear',command=clr,font=3).grid(row=3,column=0)
Button(text='Quit',command=convr.destroy,font=3).grid(row=3,column=1)

convr.mainloop()