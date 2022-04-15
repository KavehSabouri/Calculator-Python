# Kaveh Sabouri
from tkinter import *
def add():
 a = float(ent1.get()) 
 b = float(ent2.get())
 c = a + b
 result.config(text=str(c))



def subtract():
    a = float(ent1.get())
    b = float(ent2.get())
    c = a - b
    result.config(text=str(c))


def multipy():
    a = float(ent1.get())
    b = float(ent2.get())
    c = a * b
    result.config(text=str(c))

def divide():
    a = float(ent1.get())
    b = float(ent2.get())
    c = a / b
    result.config(text=str(c))



window=Tk()
window.geometry("550x500")
window.title("Calculator")
window.resizable(False,False)
f1=Frame(window,bg="lavender")
f1.pack(expand=True,fill=BOTH)
la1=Label(f1,bg="lavender",fg="red",text="First Number:",font=("",25))
la1.place(x=20,y=20)
la2=Label(f1,bg="lavender",fg="red",text="Second Number:",font=("",25))
la2.place(x=20,y=98)
ent1=Entry(f1,bg="lavender",fg="blue",bd=3)
ent1.place(x=300,y=26)
ent2=Entry(f1,bg="lavender",fg="blue",bd=3)
ent2.place(x=300,y=110)

btn1=Button(f1,bg="lavender",fg="blue",text="Add",font=("",27),command=add)
btn1.place(x=161,y=220)
btn2=Button(f1,bg="lavender",fg="blue",text="Subtract",font=("",27),command=subtract)
btn2.place(x=384,y=220)
btn3=Button(f1,bg="lavender",fg="blue",text="Multipy",font=("",27),command=multipy)
btn3.place(x=23,y=220)
btn4=Button(f1,bg="lavender",fg="blue",text="Divide",font=("",27),command=divide)
btn4.place(x=263,y=220)

Result=Label(f1,bg="lavender",fg="purple",text="Result:",font=("",29))
Result.place(x=100,y=400)

result=Label(f1,bg="lavender",fg="green",text="",font=("",29))
result.place(x=300,y=400)


window.mainloop()
