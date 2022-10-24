from cProfile import label
from ctypes import alignment
from tkinter import *

root=Tk()
root.title("Standard Calculator")
root.geometry("483x588+100+200")
root.resizable(False, False)
root.configure(bg="#21283d")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""

    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Value error"
            equation = ""
    label_result.config(text=result)

label_result = Label(root, width=28, height=2, text="", font=("arial", 26))
label_result.pack()

Button(root, text="C", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#5dc9cf", command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("/")).place(x=130, y=100)
Button(root, text="%", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("%")).place(x=250, y=100)
Button(root, text="*", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("*")).place(x=370, y=100)

Button(root, text="7", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("7")).place(x=10, y=195)
Button(root, text="8", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("8")).place(x=130, y=195)
Button(root, text="9", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("9")).place(x=250, y=195)
Button(root, text="-", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("-")).place(x=370, y=195)

Button(root, text="4", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("4")).place(x=10, y=295)
Button(root, text="5", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("5")).place(x=130, y=295)
Button(root, text="6", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("6")).place(x=250, y=295)
Button(root, text="+", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("+")).place(x=370, y=295)

Button(root, text="1", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("1")).place(x=10, y=395)
Button(root, text="2", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("2")).place(x=130, y=395)
Button(root, text="3", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("3")).place(x=250, y=395)
Button(root, text="0", width=9, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show("0")).place(x=10, y=495)

Button(root, text=".", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#334e75", command=lambda: show(".")).place(x=250, y=495)
Button(root, text="=", width=4, height=3, font=("arial", 30, "bold"), bd=1, fg="#d4dcd0", bg="#ab0a29", command=lambda: calculate()).place(x=370, y=395)




root.mainloop()