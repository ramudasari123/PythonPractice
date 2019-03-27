from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
coloring=Tk()

def colorselection():
    #button=Button(text="select color",bg='blue',command=coloring.quit()).pack()
    colorcoding=colorchooser.askcolor()
    Label(text='Your selected color',bg=colorcoding[1]).pack()

def openfile():
    fileoperation=filedialog.askopenfile()

    #File2name=fileoperation.name
    #file=open(File2name)
    #Label(text=file.read(),font=3).pack()

    Label(text=fileoperation.read(),font=3).pack()


coloring.title("Welcome User")
coloring.geometry("500x500")
label1=Label(text='ChooseColor').pack()
button1=Button(text='SelectColor',command=colorselection).pack()
button2=Button(text='open file',command=openfile,bg='green').pack()

coloring.mainloop()