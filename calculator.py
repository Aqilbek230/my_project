from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("260x380")
root.resizable(width=False,height=False)
root['bg']="snow4"

def bas(x):
    ekran.insert(END, str(x))

def tozalash():
    ekran.delete(0, END)

def hisobla():
    try:
        natija = eval(ekran.get())
        ekran.delete(0, END)
        ekran.insert(END, natija)
    except:
        ekran.delete(0, END)
        ekran.insert(END, "Xato")

Button(root,text=0,width=6,height=2,bg='white',command=lambda:bas(0)).place(x=5,y=335)
Button(root,text=".",width=6,height=2,bg='white',command=lambda:bas(".")).place(x=60,y=335)
Button(root,text="=",width=6,height=2,bg='white',command=hisobla).place(x=115,y=335)

Button(root,text=1,width=6,height=2,bg='white',command=lambda:bas(1)).place(x=5,y=290)
Button(root,text=2,width=6,height=2,bg='white',command=lambda:bas(2)).place(x=60,y=290)
Button(root,text=3,width=6,height=2,bg='white',command=lambda:bas(3)).place(x=115,y=290)

Button(root,text=4,width=6,height=2,bg='white',command=lambda:bas(4)).place(x=5,y=245)
Button(root,text=5,width=6,height=2,bg='white',command=lambda:bas(5)).place(x=60,y=245)
Button(root,text=6,width=6,height=2,bg='white',command=lambda:bas(6)).place(x=115,y=245)

Button(root,text=7,width=6,height=2,bg='white',command=lambda:bas(7)).place(x=5,y=200)
Button(root,text=8,width=6,height=2,bg='white',command=lambda:bas(8)).place(x=60,y=200)
Button(root,text=9,width=6,height=2,bg='white',command=lambda:bas(9)).place(x=115,y=200)

Button(root,text="+",width=6,height=5,bg='cyan',command=lambda:bas("+")).place(x=170,y=290)
Button(root,text="-",width=6,height=2,bg='cyan',command=lambda:bas("-")).place(x=170,y=245)
Button(root,text="*",width=6,height=2,bg='cyan',command=lambda:bas("*")).place(x=170,y=200)
Button(root,text="/",width=6,height=2,bg='cyan',command=lambda:bas("/")).place(x=170,y=155)

Button(root,text="C",width=6,height=2,bg='cyan',fg="red",command=tozalash).place(x=115,y=155)
Button(root,text="%",width=6,height=2,bg='cyan',command=lambda:bos("%")).place(x=60,y=155)
Button(root,text="off/on",width=6,height=2,bg='cyan',command=root.destroy).place(x=5,y=155)

ekran=Entry(root, font=("Arial", 18), bd=5, relief=GROOVE, justify=RIGHT)
ekran.place(x=5, y=5, width=250, height=50)
root.mainloop()
