from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")

inputs = Entry(root, width=35, borderwidth=5)
inputs.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
first_num = 0
set_symbol = None

def button_click(number):
    prev_nums = inputs.get()
    inputs.delete(0, END)
    inputs.insert(0, str(prev_nums) + str(number))

def clear_contents():
    inputs.delete(0, END)

def get_first_num(symbol):
    global first_num
    global set_symbol
    first_num = int(inputs.get())
    inputs.delete(0, END)
    set_symbol = symbol

def combine_numbers():
    global first_num
    global set_symbol
    second_num = int(inputs.get())
    inputs.delete(0, END)
    if set_symbol == "add":
        new_num = first_num + second_num
    elif set_symbol == "subtract":
        new_num = first_num - second_num
    elif set_symbol == "multiply":
        new_num = first_num * second_num
    elif set_symbol == "divide":
        new_num = int(first_num / second_num)
    inputs.insert(0, new_num)


button_0 = Button(root, text="0", padx=10, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=10, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=10, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=10, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=10, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=10, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=10, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=10, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=10, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=10, pady=20, command=lambda: button_click(9))
button_equals = Button(root, text="=", padx=10, pady=20, command=lambda: combine_numbers())
button_adds = Button(root, text="+", padx=10, pady=20, command=lambda: get_first_num("add"))
button_subtracts = Button(root, text="-", padx=10, pady=20, command=lambda: get_first_num("subtract"))
button_multiplies = Button(root, text="*", padx=10, pady=20, command=lambda: get_first_num("multiply"))
button_divides = Button(root, text="/", padx=10, pady=20, command=lambda: get_first_num("divide"))
button_clear = Button(root, text="Clear", padx=10, pady=20, command=lambda: clear_contents())

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equals.grid(row=4, column=2)

button_adds.grid(row=5, column=0)
button_subtracts.grid(row=5, column=1)

button_multiplies.grid(row=6, column=0)
button_divides.grid(row=6, column=1)

root.mainloop()
