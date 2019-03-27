from tkinter import *

Rbuttons=Tk()
Rbuttons2=Tk()
Rbuttons.title("Radio Butt Demo")
Rbuttons.geometry("500x500")
Rbuttons2.title('Welcome to Window-2')
Rbuttons2.geometry("500x500")

def MaritalStatus():
    status=a.get()
    if(status==1):
        Label(text='***we are verifying your status..Please wait***',font=3).pack()
    if(status==2):
        Label(text='***Enjoy your bachelor life***',font=3).pack()
    if(status==3):
        Label(text='***Happy married Life***',font=3).pack()
    if(status==4):
        Label(text='***sorry, we didnt found Try again***',font=3).pack()

ButtonsList=[("Tesnion",1),("Happy",2),("Unhappy",3),("Confusion",4)]##this list is called in the second window to create radio buttons from a list

a=IntVar()
a.set(3)

button1=Radiobutton(text='verify',variable=a,value=1,bg='Red',padx=20,command=MaritalStatus).pack()##padx makes the button size padding
button2=Radiobutton(text='unmarried',variable=a,value=2,bg='Green',command=MaritalStatus).pack(anchor=W)##anchor moves positin of button on screen
button3=Radiobutton(text='Married',variable=a,value=3,bg='Blue',command=MaritalStatus).pack()## Value allows to select any one radio button
button4=Radiobutton(text='None',variable=a,value=4,bg='Yellow',command=MaritalStatus).pack()##set to 3, makes default selection o button as3

for txt, values in ButtonsList:
    Radiobutton(Rbuttons2,text=txt,variable=a,value=values,font=3,indicatoron=0,width=15,justify=LEFT,command=MaritalStatus).pack(anchor=W)

Rbuttons.mainloop()