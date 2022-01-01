from tkinter import *
from tkinter.ttk import *
from sys import exit
root = Tk()

k = 0

root.title("Happy Brithday!")

root.geometry('650x400')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label="Menu Thing")
menu.add_cascade(label="File", menu=item)
menu.add_cascade(label="Stuff", menu=item)
root.config(menu=menu)

#: adding a label to the root window
lbl = Label(root, text = "Are you a happy?")
lbl.grid()

#: what occurs after getting clicked
txt = Entry(root, width=10)
txt.grid(column =1, row =1)

def clicked():
    global k
    k += 1
    res = "You wrote: " + txt.get()
    lbl.configure(text = res + str(k))

#: button widget with red color text inside
btn = Button(root, text = "Click me", command=clicked)
#: defining button size
btn.grid(column=1, row=0)


def countdown():
    global k
    if k == 0:
        message = Label(root, text = "3...")
    elif k == 1:
        message = Label(root, text = "2...")
    elif k == 2:
        message = Label(root, text = "1...")
    else:
        message = Label(root, text = "Blast off!")
    k += 1
    message.grid()

new_button = Checkbutton(root, text = "1st", command=countdown)
new_button.grid(column=4, row=3)


def leave():
    exit()

leave_button = Button(root, text = "Click me and you're done!", command=leave)
leave_button.grid(column=5, row=5)

root.mainloop()
