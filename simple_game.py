from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()
root.title("Simple Investor")
root.geometry("900x450")

pl_money = 100
turn_count = -1
total_turns = 5

def get_randoms():
    global market_value
    global value_mod
    market_value = random.randrange(-100, 101)
    value_mod = random.randrange(-65, 66)

first_frame = LabelFrame(root, text="Invest Here", padx=10, pady=10)
first_frame.grid(row=0, column=0)

enter_number_label = Label(first_frame, text=f"You start with ${pl_money}. How much would you like to invest?")
enter_number_label.grid()

number_box = Entry(first_frame)
number_box.grid()

number_button = Button(first_frame, text="Submit Amount", command=lambda: [
get_new_amt(),
update_turn_show(),
outlook_gen(),
set_outlook()
])
number_button.grid()


#: Second Frame
second_frame = LabelFrame(root, text="Market Overview", padx=10, pady=10)
second_frame.grid(row=0, column=1, padx=10)

def outlook_gen():
    global turn_count
    if turn_count == -1:
        get_randoms()
    elif turn_count == 0:
        get_randoms()
    elif turn_count >= 1:
        get_randoms()
    turn_count += 1

outlook_gen()

def return_outlook():
    global value_mod
    global market_value
    hidden_value = value_mod + market_value
    #: print(f"value_mod is: {value_mod} and market_value is: {market_value}.")
    if hidden_value >= 75 or hidden_value <= -75:
        return  "extreme volatility"
    elif hidden_value <= 75 and hidden_value >= 45:
        return  "moderate volatility"
    elif hidden_value >= -75 and hidden_value <= -45:
        return  "moderate volatility"
    elif hidden_value <= 45 and hidden_value >= 15:
        return "decent volatility"
    elif hidden_value >= -45 and hidden_value <= -15:
        return "decent volatility"
    elif hidden_value <= 15 and hidden_value >= -15:
        return  "little volatility"

def set_outlook():
    global turn_count
    global total_turns
    #: print(f"The turn_count is: {turn_count}")
    if turn_count == 0:
        return
    elif turn_count < total_turns:
        market_outlook = Label(second_frame, text=f"For turn {turn_count + 1}, there is {return_outlook()} in the market.")
    elif turn_count == total_turns:
        market_outlook = Label(second_frame, text=f"The market is closed.")
    elif turn_count > total_turns:
        return
    market_outlook.grid()

set_outlook()
market_outlook_og = Label(second_frame, text=f"For turn {turn_count + 1}, there is {return_outlook()} in the market.")
market_outlook_og.grid()


#: Third Frame
third_frame = LabelFrame(root, text="", padx=10, pady=10)
third_frame.grid(row=1, column=0)

def get_new_amt():
    global pl_money
    global turn_count
    global total_turns

    if pl_money <= 0 and turn_count <= total_turns:
        answer = Label(third_frame, text=f"You've lost all your money. You lose.")
        turn_count = total_turns
        set_outlook()
    elif turn_count == total_turns and pl_money > 0:
        answer = Label(third_frame, text=f"You finished the game with ${pl_money}. Congrats!")
    elif turn_count > total_turns:
        return
    elif turn_count < total_turns:
        amt_invested = int(number_box.get())
        if amt_invested > pl_money:
            amt_invested = pl_money
        new_amt = amt_invested + (amt_invested * (market_value * 0.01))
        pl_money -= amt_invested
        pl_money += new_amt
        if pl_money <= 0:
            get_new_amt()
            return
        answer = Label(third_frame, text=f"After turn {turn_count + 1}, you have ${pl_money} left.")
    answer.grid()


#: Fourth Frame
fourth_frame = LabelFrame(root, text="Turns Remaining", padx=10, pady=10)
fourth_frame.grid(row=0, column=3)

total_turns_show = Label(fourth_frame, text=f"There are {total_turns} turns in this simulation.")
total_turns_show.grid()

def update_turn_show():
    remaining_turns = total_turns - turn_count - 1
    if remaining_turns <= -1:
        return
    elif remaining_turns >= 0:
        turn_show = Label(fourth_frame, text=f"There are {total_turns - turn_count - 1} turns left.")
        turn_show.grid()


#: Misc.
exit_game = Button(root, text="Exit Game", command=root.quit).grid(column=3)

def welcome_message():
    if turn_count == 0:
        messagebox.showinfo("", "Welcome to this investment simulator!\n\nLet's see how much money you can make!")
    elif turn_count > 0:
        pass

welcome_message()
root.mainloop()
