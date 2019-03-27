from tkinter import *

#data1=StringVar()
def message():
   # textgiven=data1.get()
    Label(text="*********Welcome user***********", fg="Red", bg="white",font=10).pack()

def SaveMessage():
    Label(text='Hi User')
    mylabel5=Label(text='file save as is success',font=('arial',22,'itaic'))

def deleteBox():
    Label(text='u want to delete?')


gui = Tk()
sw=Tk()
sw.title("Hi I am dual......")
gui.title("Hi......")
gui.geometry("500x500+100+100")
sw.geometry("400x400+100+100")

#Mylabel = Label(text="***Welcome***",fg="green",bg="yellow").place(x=100,y=100)
#Mylabel.pack()
#Mylabel3 = Label(text="***oyy***",fg="green",bg="yellow").grid(row=0,column=0,sticky='w')
swlabel=Label(sw,text='Hi People',fg='blue',bg='white').pack()
Mylabel = Label(text="***Welcome***",fg="green",bg="yellow").pack()
Mylabel2 = Label(text="***RAM DASARI***",fg="Red",bg="white",font=('arial',22,'italic')).pack()
mybutton1= Button(text='clickMe',fg="grey",bg='white',command=message,font=10).pack()

#textBox = Entry(textvariable=data1).pack()
textBox = Entry().pack()

######File Menu List of Operatins###
FileMenuList=Menu()
FileMenuList.add_cascade(label='Edit')
FileMenuList.add_cascade(label='Open')
FileMenuList.add_cascade(label='Save')
FileMenuList.add_cascade(label='SaveAs',command=SaveMessage)
FileMenuList.add_cascade(label='Delete',command=deleteBox)

######Edit Menu List of Operatins###
EditMenuList=Menu()
EditMenuList.add_cascade(label='EditFile')
EditMenuList.add_cascade(label='EditPrevious')
EditMenuList.add_cascade(label='EditAll')



mymenu= Menu()
mymenu.add_cascade(label="File",menu=FileMenuList)
mymenu.add_checkbutton(label='Find')
mymenu.add_cascade(label='Edit',menu=EditMenuList)
mymenu.add_radiobutton(label='Help',command='WelcomeMessage')
gui.config(menu=mymenu)

sw.mainloop()
gui.mainloop()