import tkinter as tk
import subprocess

# Open games
def open_simple_shooter():
    subprocess.Popen(["python", "games\\simple_shooter\\simple_shooter.py"])
    
def open_guess_the_number():
    subprocess.Popen(["python", "games\\guess_the_number\\guess_the_number.py"])

def open_dino_game():
    subprocess.Popen(["games\\dino_game\\dinoGame.exe"], creationflags=subprocess.CREATE_NEW_CONSOLE)

# Create main window
root = tk.Tk()
root.title("GameHub")
root.geometry("600x300")

# Title Label
label = tk.Label(root, text="Choose a Game", font=("Arial", 14))
label.pack(pady=10)

# Buttons to launch games or exit
btn_game1 = tk.Button(root, text="Simple Shooter", command=open_simple_shooter, font=("Arial", 12))
btn_game1.pack(pady=10)

btn_game2 = tk.Button(root, text="Guess The Number", command=open_guess_the_number, font=("Arial", 12))
btn_game2.pack(pady=10)

btn_game3 = tk.Button(root, text="Dino Game", command=open_dino_game, font=("Arial", 12))
btn_game3.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", command=exit, font=("Arial", 12))
btn_exit.pack(pady=10)

# Run the Tkinter loop
root.mainloop()