import tkinter as tk
from tkinter import messagebox
import random

CHOICES = ["Rock", "Paper", "Scissors"]

def play():
    user_pick = entry_choice.get().strip().capitalize()

    if user_pick not in CHOICES:
        messagebox.showwarning("Invalid choice", "Please type Rock, Paper, or Scissors.")
        return

    # 7) Generate random selection for the computer
    # 8) Assign it to comp_pick
    comp_pick = random.choice(CHOICES)

    result_label.config(
        text=f"You chose: {user_pick}\nComputer chose: {comp_pick}"
    )

# --- UI ---
root = tk.Tk()

# 2) Initialize game window with title and dimensions
root.title("Rock Paper Scissors - Phase 1")
root.geometry("420x260")
root.resizable(False, False)

# 3) Background color
root.configure(bg="white")

# 4) Title label
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="white")
title.pack(pady=10)

# 5) Prompt user to choose
prompt = tk.Label(root, text="Type Rock, Paper, or Scissors:", font=("Arial", 12), bg="white")
prompt.pack()

# 6) Input field
entry_choice = tk.Entry(root, width=20)
entry_choice.pack(pady=8)

# Button to play
play_btn = tk.Button(root, text="Play", width=12, command=play)
play_btn.pack(pady=8)

# Result display
result_label = tk.Label(root, text="Make your choice and press Play.", font=("Arial", 11), bg="white")
result_label.pack(pady=10)

root.mainloop()
