from tkinter import *

root = Tk()
root.title("My Calculator")



e = Entry(root, width=35, borderwidth=5)

width = 40
height = 30

def clickNum(num):
    e.insert("end", str(num))


def clickOp(op):
    global op1
    op1 = float(e.get())
    e.delete(0, END)
    global oper
    oper = op


def calc():
    global op2
    op2 = float(e.get())
    e.delete(0, END)
    result = 0
    if(oper == '+'):
        result = op1 + op2
    elif(oper == '-'):
        result = op1 - op2
    elif(oper == '*'):
        result = op1 * op2
    else:
        result = op1 / op2

    e.insert(0, result)

def clear():
    e.delete(0, END)


button1 = Button(root, text="1", padx =width, pady = height, command = lambda: clickNum(1))
button2 = Button(root, text="2", padx =width, pady = height, command = lambda: clickNum(2))
button3 = Button(root, text="3", padx =width, pady = height, command = lambda: clickNum(3))
button4 = Button(root, text="4", padx =width, pady = height, command = lambda: clickNum(4))
button5 = Button(root, text="5", padx =width, pady = height, command = lambda: clickNum(5))
button6 = Button(root, text="6", padx =width, pady = height, command = lambda: clickNum(6))
button7 = Button(root, text="7", padx =width, pady = height, command = lambda: clickNum(7))
button8 = Button(root, text="8", padx =width, pady = height, command = lambda: clickNum(8))
button9 = Button(root, text="9", padx =width, pady = height, command = lambda: clickNum(9))
button0 = Button(root, text="0", padx =width, pady = height, command = lambda: clickNum(0))
button_add = Button(root, text="+", padx =width, pady = height, command = lambda: clickOp("+"))
button_sub = Button(root, text="-", padx =width, pady = height, command = lambda: clickOp("-"))
button_multiply = Button(root, text="x", padx =width, pady = height, command = lambda: clickOp("*"))
button_divide = Button(root, text="/", padx =width, pady = height, command = lambda: clickOp("/"))
button_equal = Button(root, text="=", padx =width * 2 + 10, pady = height, command = lambda: calc())
button_clear = Button(root, text="Clear", padx=width - 10, pady=height, command =clear)
bname = "button"
#showing ontoscreen
e.grid(row = 0, column= 0, columnspan = 3)
button_clear.grid(row = 0, column = 3)
button0.grid(row=4, column=0)
button1.grid(row= 1, column = 0)
button2.grid(row= 1, column = 1)
button3.grid(row= 1, column = 2)
button4.grid(row= 2, column = 0)
button5.grid(row= 2, column = 1)
button6.grid(row= 2, column = 2)
button7.grid(row= 3, column = 0)
button8.grid(row= 3, column = 1)
button9.grid(row= 3, column = 2)

button_add.grid(row = 1, column = 3)
button_sub.grid(row = 2, column = 3)
button_multiply.grid(row = 3, column = 3)
button_divide.grid(row = 4, column = 3)
button_equal.grid(row = 4, column = 1, columnspan = 2)

root.mainloop()
