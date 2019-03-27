from tkinter import *

check=Tk()
check.geometry('500x500')
def PrintValues():
    print(a1.get(),a2.get(),a3.get(),a4.get())
    data=a1.get()+a2.get()+a3.get()+a4.get()
    Label(text=data).pack()###print number of checked values on window

EditList=Menu()
EditList.add_cascade(label='save')
EditList.add_checkbutton(label='SaveAs')
check.config()

MenuItems=Menu()
MenuItems.add_cascade(label='Edit',menu=EditList)
MenuItems.add_command(label='File')
check.config(menu=MenuItems)


a1=IntVar()
btn1=Checkbutton(text='btn1',variable=a1).pack()
a2=IntVar()
btn1=Checkbutton(text='btn2',variable=a2).pack()
a3=IntVar()
btn1=Checkbutton(text='btn3',variable=a3).pack()
a4=IntVar()
btn1=Checkbutton(text='btn4',variable=a4).pack()

Button(text='ClickAny',command=PrintValues,font=3).pack()
Button(text='Close',command=check.destroy).pack()


check.mainloop()