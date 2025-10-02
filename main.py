import random
import tkinter as tk

options = {'rock': '✊', 'paper': '✋', 'scissors': '✌️'}
choices = list(options.keys())

def play(game_choice):
    computer_choice = random.choice(choices)
    player_emoji = options[game_choice]
    computer_emoji = options[computer_choice]
    if game_choice == computer_choice:
        result = "It's a tie!"
    elif(game_choice == 'rock' and computer_choice == 'scissors') or \
        (game_choice == 'paper' and computer_choice == 'rock') or \
        (game_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "Computer wins!"
    result_label.config(
        text=f"You chose {game_choice.capitalize()} {player_emoji}\n"
        f"Computer chose {computer_choice.capitalize()} {computer_emoji}\n"
        f"{result}"
    )

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

title_label = tk.Label(root, text = "Choose your move:", font = ("Arial Black", 14), fg = "Black")
title_label.pack(pady = (20, 10))

button_frame = tk.Frame(root, bg = "White")
button_frame.pack(pady = 10)

for choice in choices:
    tk.Button(
        button_frame,
        text = f"{choice.capitalize()} {options[choice]}",
        font = ("Arial Black", 10),
        fg = "Red",
        activebackground= "LightGray",
        activeforeground= "Black",
        bg = "White",
        bd = 4,
        relief = "raised",
        command = lambda c = choice: play(c)).pack(fill='x')

result_label = tk.Label(root, text = "", font = ("Arial Black", 14))
result_label.pack(pady = 20)
root.mainloop()