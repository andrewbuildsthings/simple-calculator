from functools import partial
from tkinter import *


root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#functions (0-9, +, -, *, /, =, clear)
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num 
    global math 
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_sub():
    first_number = e.get()
    global f_num 
    global math 
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num 
    global math 
    math = "mul"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num 
    global math 
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, f_num + int(second_number))

    if math == "sub":
        e.insert(0, f_num - int(second_number))

    if math == "mul":
        e.insert(0, f_num * int(second_number))

    if math == "div":
        e.insert(0, f_num / int(second_number))


#buttons
button_0 = Button(root, text="0", bg="#cfcfd8", padx=40, pady=20, command=partial(button_click, 0))
button_0.grid(row=4, column=0)

button_1 = Button(root, text="1", bg="#cfcfd8", padx=40, pady=20, command=partial(button_click, 1))
button_1.grid(row=3, column=0)

button_2 = Button(root, text="2", bg="#cfcfd8", padx=40, pady=20, command=partial(button_click, 2))
button_2.grid(row=3, column=1)

button_3 = Button(root, text="3", bg="#cfcfd8", padx=40, pady=20, command=partial(button_click, 3))
button_3.grid(row=3, column=2)

button_4 = Button(root, text="4", bg="#cfcfd8", padx=40, pady=20, command=partial(button_click, 4))
button_4.grid(row=2, column=0)

button_5 = Button(root, text="5", bg="#cfcfd8", padx=40, pady=20, command=partial(button_click, 5))
button_5.grid(row=2, column=1)

button_6 = Button(root, text="6", bg="#cfcfd8", padx=40, pady=20, command=partial(button_click, 6))
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", bg="#cfcfd8", padx=40, pady=20, command=partial(button_click, 7))
button_7.grid(row=1, column=0)

button_8 = Button(root, text="8", bg="#cfcfd8", padx=40, pady=20, command=partial(button_click, 8))
button_8.grid(row=1, column=1)

button_9 = Button(root, text="9", bg="#cfcfd8", padx=40, pady=20, command=partial(button_click, 9))
button_9.grid(row=1, column=2)

button_add = Button(root, text="+", bg="#e0dab5", padx=40, pady=20, command=button_add)
button_add.grid(row=4, column=3)

button_sub = Button(root, text="-", bg="#e0dab5", padx=40, pady=20, command=button_sub)
button_sub.grid(row=3, column=3)

button_mul = Button(root, text="*", bg="#e0dab5", padx=40, pady=20, command=button_mul)
button_mul.grid(row=2, column=3)

button_div = Button(root, text="/", bg="#e0dab5", padx=40, pady=20, command=button_div)
button_div.grid(row=1, column=3)

button_tot = Button(root, text="=", bg="#e0dab5", padx=40, pady=20, command=button_equal)
button_tot.grid(row=4, column=2)

button_clr = Button(root, text="C", bg="#a3c9ec", padx=40, pady=20, command=button_clear)
button_clr.grid(row=4, column=1)


root.mainloop()