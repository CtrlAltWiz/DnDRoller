import tkinter as tk
from tkinter import ttk
import random

# D&D Dice Roller
# by CtrlAltWiz
# https://github.com/CtrlAltWiz

# Initialize a dictionary to store roll results
roll_results = {}

def roll_dice():
    selected_dice = dice_combobox.get()
    num_rolls = int(rolls_entry.get())
    roll_modifier = int(modifier_entry.get())
    modifier_operation = modifier_operation_combobox.get()

    if selected_dice == "":
        result_label.config(text="Please select a dice type.")
        return

    sides = int(selected_dice.split("d")[1])

    # Roll the dice and store the original results
    original_results = [random.randint(1, sides) for _ in range(num_rolls)]

    # Apply the roll modifier based on the selected operation
    if modifier_operation == "+":
        results_with_modifier = [result + roll_modifier for result in original_results]
    else:
        results_with_modifier = [result - roll_modifier for result in original_results]

    # Store the results in the dictionary
    if selected_dice in roll_results:
        roll_results[selected_dice].extend(results_with_modifier)
    else:
        roll_results[selected_dice] = results_with_modifier

    result_label.config(text=f"You rolled a {selected_dice} {num_rolls} times, with a modifier of {roll_modifier} ({modifier_operation}):\n"
                            f"Original results: {original_results}\n"
                            f"Modified results: {results_with_modifier}\n"
                            f"Total {selected_dice} rolls with modifier: {roll_results[selected_dice]}")

def reset_tally():
    roll_results.clear()
    result_label.config(text="Total reset.")
    
# Create the main window
window = tk.Tk()
window.title("D&D Dice Roller")

# Create and configure widgets
dice_label = ttk.Label(window, text="Select Dice:")
dice_options = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
dice_combobox = ttk.Combobox(window, values=dice_options)

rolls_label = ttk.Label(window, text="Number of Rolls:")
rolls_entry = ttk.Entry(window)

modifier_label = ttk.Label(window, text="Roll Mod:")
modifier_entry = ttk.Entry(window)

modifier_operation_label = ttk.Label(window, text="Modifier:")
modifier_operation_options = ["+", "-"]
modifier_operation_combobox = ttk.Combobox(window, values=modifier_operation_options)

roll_button = ttk.Button(window, text="Roll", command=roll_dice)
reset_button = ttk.Button(window, text="Reset Total", command=reset_tally)
result_label = ttk.Label(window, text="")

# Place widgets on the window using grid layout
dice_label.grid(row=0, column=0)
dice_combobox.grid(row=0, column=1)
rolls_label.grid(row=1, column=0)
rolls_entry.grid(row=1, column=1)
modifier_label.grid(row=2, column=0)
modifier_entry.grid(row=2, column=1)
modifier_operation_label.grid(row=3, column=0)
modifier_operation_combobox.grid(row=3, column=1)
roll_button.grid(row=4, column=0)
reset_button.grid(row=4, column=1)
result_label.grid(row=5, columnspan=2)

# Start the Tkinter main loop
window.mainloop()
