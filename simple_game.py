from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("My Simple Game")
root.geometry("650x450")

pl_money = 100
main_message = f"You have {pl_money} money. How much would you like to invest?"

#: First Frame
first_frame = LabelFrame(root, text="Q1", padx=10, pady=10)
first_frame.grid(row=0, column=0)

def get_number():
    global pl_money
    pl_money -= int(number_box.get())
    answer = Label(first_frame, text=f"You have {pl_money} money left.")
    answer.grid()

enter_number_label = Label(first_frame, text=main_message)
enter_number_label.grid()

number_box = Entry(first_frame)
number_box.grid()

number_button = Button(first_frame, text="Enter the number", command=get_number)
number_button.grid()

#: Second Frame
second_frame = LabelFrame(root, text="Market Overview", padx=10, pady=10)
second_frame.grid(row=0, column=1)
market_value = random.randrange(0, 9)

def outlook_gen():
    global market_value
    value_mod = random.randrange(0, 4)
    operator_mod = random.randrange(0, 2)

    if operator_mod == 0:
        hidden_value = market_value + value_mod
    elif operator_mod == 1:
        hidden_value = market_value - value_mod

    if hidden_value >= 6:
        return "great"
    elif hidden_value < 6 and hidden_value > 0:
        return "decent"
    elif hidden_value <= 0 and hidden_value > -6:
        return "not great"
    elif hidden_value <= -6:
        return "poor"


market_outlook = Label(second_frame, text=f"The market is looking {outlook_gen()}.")
market_outlook.grid()



exit_game = Button(root, text="Exit Game", command=root.quit).grid(column=2)

root.mainloop()
