from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()
root.title("My Simple Game")
root.geometry("650x450")

pl_money = 100
turn_count = 0

def get_randoms():
    global market_value
    global value_mod
    market_value = random.randrange(-100, 101)
    value_mod = random.randrange(-65, 66)

#: First Frame
first_frame = LabelFrame(root, text="Q1", padx=10, pady=10)
first_frame.grid(row=0, column=0)


def get_new_amt():
    global pl_money
    global turn_count
    turn_count += 1

    def delete_old_info():
        if turn_count > 0:
            pass # TODO: delete the old "answer.grid"

    if turn_count > 1:
        get_randoms()

    if pl_money <= 0:
        answer = Label(first_frame, text=f"You've lost all your money. You lose.")
    elif turn_count >= 4:
        answer = Label(first_frame, text=f"You finished the game with ${pl_money}.")
    elif turn_count < 4:
        amt_invested = int(number_box.get())
        new_amt = amt_invested + (amt_invested * (market_value * 0.1))
        pl_money -= amt_invested
        pl_money += new_amt
        if pl_money < 0:
            pl_money = 0
        answer = Label(first_frame, text=f"After turn {turn_count}, you have ${pl_money} left.")

    delete_old_info()
    answer.grid()

main_message = f"You have ${pl_money}. How much would you like to invest?"
enter_number_label = Label(first_frame, text=main_message)
enter_number_label.grid()

number_box = Entry(first_frame)
number_box.grid()

number_button = Button(first_frame, text="Enter the number", command=lambda: [get_new_amt()])
number_button.grid()

#: Second Frame

second_frame = LabelFrame(root, text="Market Overview", padx=10, pady=10)
second_frame.grid(row=0, column=1)

def outlook_gen():
    global value_mod
    global market_value
    if turn_count == 0:
        get_randoms()
    hidden_value = value_mod + market_value
    if hidden_value >= 65:
        return "great"
    elif hidden_value < 65 and hidden_value > 25:
        return "decent"
    elif hidden_value <= 25 and hidden_value > -25:
        return "not great"
    elif hidden_value <= -25 and hidden_value > -65:
        return "poor"
    elif hidden_value <= -65:
        return "bad"

market_outlook = Label(second_frame, text=f"The market is looking {outlook_gen()}.")
market_outlook.grid()


exit_game = Button(root, text="Exit Game", command=root.quit).grid(column=2)

def welcome_message():
    if turn_count == 0:
        messagebox.showinfo("", "Welcome to this investment simulator!\n\nLet's see how much money you can make!")
    elif turn_count > 0:
        pass

welcome_message()
root.mainloop()
