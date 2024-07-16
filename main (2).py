import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
root.title("Treasure Island")

# Add a label for the game title
title_label = tk.Label(root, text="Welcome to Treasure Island!", font=("Arial", 16))
title_label.pack(pady=20)

# Create a text area for displaying game text
text_area = tk.Text(root, wrap=tk.WORD, height=10, width=50)
text_area.pack(pady=10)

# Define the characters and events
characters = ["hero", "heroine", "villain"]
events = ["You found a hidden path!", "A wild animal appears!", "You discover a mysterious artifact!", "You hear strange whispers in the wind."]

# Introduce the hero
def start_game():
    text_area.delete("1.0", tk.END)  # Clear previous text
    text_area.insert(tk.END, "You are the hero on a quest to find the hidden treasure on Treasure Island.\n")
    show_crossroads()

def show_crossroads():
    text_area.delete("1.0", tk.END)  # Clear previous text
    text_area.insert(tk.END, "You're at a crossroad. Where do you want to go?\n")
    left_button = tk.Button(root, text="Left", command=lambda: handle_choice("L"))
    left_button.pack(pady=5)
    right_button = tk.Button(root, text="Right", command=lambda: handle_choice("R"))
    right_button.pack(pady=5)

def handle_choice(choice):
    text_area.delete("1.0", tk.END)
    global villain_door
    villain_door = random.choice(["Red", "Blue", "Yellow"])

    if choice == "L":
        text_area.insert(tk.END, "You have met the heroine who warns you about the villain.\n")
        show_river()
    elif choice == "R":
        text_area.insert(tk.END, f"You encounter the villain and he traps you behind the {villain_door} door. Game over!\n")
        end_game("You lost!")
    else:
        text_area.insert(tk.END, "Invalid choice. Game over!\n")
        end_game("Invalid choice")

def show_river():
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, "You arrive at a river. Do you want to swim across or wait for a boat?\n")
    swim_button = tk.Button(root, text="Swim", command=lambda: handle_river("S"))
    swim_button.pack(pady=5)
    wait_button = tk.Button(root, text="Wait", command=lambda: handle_river("W"))
    wait_button.pack(pady=5)

def handle_river(choice):
    text_area.delete("1.0", tk.END)
    if choice == "S":
        text_area.insert(tk.END, "You get attacked by a sea monster. Game over!\n")
        end_game("You lost!")
    elif choice == "W":
        text_area.insert(tk.END, "You and the heroine wait patiently and find a boat. You arrive safely across the river.\n")
        text_area.insert(tk.END, f"{random.choice(events)}\n")
        show_doors()

def show_doors():
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, "You find three doors: Red, Blue, and Yellow. Which door do you choose?\n")
    red_button = tk.Button(root, text="Red", command=lambda: handle_door("R"))
    red_button.pack(pady=5)
    blue_button = tk.Button(root, text="Blue", command=lambda: handle_door("B"))
    blue_button.pack(pady=5)
    yellow_button = tk.Button(root, text="Yellow", command=lambda: handle_door("Y"))
    yellow_button.pack(pady=5)

def handle_door(choice):
    text_area.delete("1.0", tk.END)
    if choice == villain_door[0].upper():
        text_area.insert(tk.END, f"The villain was hiding behind the {villain_door} door. Game over!\n")
        end_game("You lost!")
    elif choice == "Y":
        text_area.insert(tk.END, "You find the treasure and win!\n")
        end_game("You won!")
    else:
        text_area.insert(tk.END, "You chose a wrong door. Game over!\n")
        end_game("You lost!")

def end_game(message):
    messagebox.showinfo("Treasure Island", message)
    root.destroy()

# Start the game
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()