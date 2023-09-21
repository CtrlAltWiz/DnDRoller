import tkinter as tk
from tkinter import ttk
import random

# D&D Dice Roller
# by CtrlAltWiz
# https://github.com/CtrlAltWiz

def roll_dice():
    selected_dice = dice_combobox.get()
    num_rolls = int(rolls_entry.get())

    if selected_dice == "":
        result_label.config(text="Please select a dice type.")
        return

    sides = int(selected_dice.split("d")[1])

    results = [random.randint(1, sides) for _ in range(num_rolls)]
    result_label.config(text=f"You rolled a {selected_dice} {num_rolls} times: {results}")

# Create the main window
window = tk.Tk()
window.title("Dice Roller")

# Create and configure widgets
dice_label = ttk.Label(window, text="Select Dice:")
dice_options = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
dice_combobox = ttk.Combobox(window, values=dice_options)

rolls_label = ttk.Label(window, text="Number of Rolls:")
rolls_entry = ttk.Entry(window)

roll_button = ttk.Button(window, text="Roll", command=roll_dice)
result_label = ttk.Label(window, text="")

# Place widgets on the window using grid layout
dice_label.grid(row=0, column=0)
dice_combobox.grid(row=0, column=1)
rolls_label.grid(row=1, column=0)
rolls_entry.grid(row=1, column=1)
roll_button.grid(row=2, columnspan=2)
result_label.grid(row=3, columnspan=2)

# Start the Tkinter main loop
window.mainloop()
