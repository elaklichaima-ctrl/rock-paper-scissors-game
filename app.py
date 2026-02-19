import tkinter as tk
from tkinter import messagebox
import random

CHOICES = ["Rock", "Paper", "Scissors"]

# 1️⃣ Game Logic Function
def play():
    user_pick = entry_choice.get().strip().capitalize()

    if user_pick not in CHOICES:
        messagebox.showwarning("Invalid choice", "Please type Rock, Paper, or Scissors.")
        return

    comp_pick = random.choice(CHOICES)

    # 2️⃣ Conditional statements to determine winner
    if user_pick == comp_pick:
        result = "It's a Draw 🤝"
    elif (user_pick == "Rock" and comp_pick == "Scissors") or \
         (user_pick == "Paper" and comp_pick == "Rock") or \
         (user_pick == "Scissors" and comp_pick == "Paper"):
        result = "You Win 🎉"
    else:
        result = "Computer Wins 💻"

    result_label.config(
        text=f"You: {user_pick}\nComputer: {comp_pick}\nResult: {result}"
    )

# 3️⃣ Reset Function
def Reset():
    entry_choice.delete(0, tk.END)
    result_label.config(text="Make your choice and press Play.")

# 4️⃣ Exit Function
def Exit():
    root.destroy()

# --- UI ---
root = tk.Tk()
root.title("Rock Paper Scissors - Phase 2")
root.geometry("420x300")
root.resizable(False, False)
root.configure(bg="white")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="white")
title.pack(pady=10)

prompt = tk.Label(root, text="Type Rock, Paper, or Scissors:", font=("Arial", 12), bg="white")
prompt.pack()

entry_choice = tk.Entry(root, width=20)
entry_choice.pack(pady=8)

btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Play", width=10, command=play).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Reset", width=10, command=Reset).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Exit", width=10, command=Exit).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="Make your choice and press Play.", font=("Arial", 11), bg="white")
result_label.pack(pady=10)

root.mainloop()
