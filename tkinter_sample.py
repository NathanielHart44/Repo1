from tkinter import *
from tkinter import messagebox

win = Tk()

"""
number = 1
number_2 = 2

def set_text(text):
    e.delete(0,END)
    if text == "animal":
        e.insert(0,number)
    else:
        e.insert(0,number_2)

a = Entry(win,width=10).grid()

e = Entry(win,width=10)
e.grid()

b1 = Button(win,text=a,command=lambda:set_text("animal"))
b1.grid()

b2 = Button(win,text="plant",command=lambda:set_text("plant"))
b2.grid()"""
pl_money = 100
main_message = f"You have {pl_money} money. How much would you like to invest?"

def get_number():
    global pl_money
    pl_money -= int(number_box.get())
    answer = Label(win, text=f"You have {pl_money} money left.")
    answer.grid()

enter_number_label = Label(win, text=main_message)
enter_number_label.grid()

number_box = Entry()
number_box.grid()

number_button = Button(win, text="Enter the number", command=get_number)
number_button.grid()

messagebox.showinfo("Hello", "You're great!")

win.mainloop()
