from tkinter import *
from tkinter import ttk
from tkinter import messagebox
window=Tk()
window.title("Temperature convertor")
window.geometry("400x600")
window.minsize(400,600)
window.maxsize(400,600)

## define input box
temp=StringVar()
click=StringVar()

## define buttons
def convert():

    if temp.get()=="":
        messagebox.showerror("Temperature convertor","Input field is blank")

    elif(click.get()=="Choose option"):
        messagebox.showerror("Temperature convertor","Please select any option")

    elif(click.get()=="Celsius"):
        result=(5/9)*(int(temp.get())-32)
        label.config(text=result,font=("",13,"bold"),fg="#bc2124")

    elif(click.get()=="Fahrenheit"):
        result=int(temp.get())*(9/5)+32
        label.config(text=result,font=("",13,"bold"),fg="#06656d")


def Exit():
    exit(0)
## define headings
Label(window,text=" ").pack(pady=10)
Label(window,text="Temperature convertor ",font=("deja vu sans",18,""),).pack()
Label(window,text="celsius & fahrenheit ",font=("",11,"")).pack()

## define frames
frame=Frame(window)
frame.pack(anchor="n",pady=20,padx=5)
Label(frame,text="Enter temperature: ",font=("",12,"")).grid(row=0,column=0)
Entry(frame,textvariable=temp,width="25").grid(row=0,column=1)
Label(window,text="convert into...",font=("",10,"")).pack(anchor="n",pady=5)

##define drop down menu
data=["Celsius","Fahrenheit"]
click.set("Choose option")
OptionMenu(window,click,*data).pack(anchor="n")
Button(text="Convert",font=("",11,"bold"),bg="#0bd5e8",command=convert).pack(pady=10)
Button(text="Exit",font=("",11,"bold"),bg="#f4755f",command=Exit).pack()

## define blank label for config
label=Label(window,text=" ")
label.pack(pady=6)
window.mainloop()