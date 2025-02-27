import tkinter as tk
import subprocess


# Open games
def open_simple_shooter():
    root.withdraw()
    subprocess.Popen(["python", "games\\simple_shooter\\simple_shooter.py"]).wait()
    root.deiconify()
    
def open_guess_the_number():
    root.withdraw()
    subprocess.Popen(["python", "games\\guess_the_number\\guess_the_number.py"]).wait()
    root.deiconify()

def open_dino_game():
    root.withdraw()
    subprocess.Popen(["games\\dino_game\\dinoGame.exe"], creationflags=subprocess.CREATE_NEW_CONSOLE).wait()
    root.deiconify()
    
def open_rock_paper_scissors():
    root.withdraw()
    subprocess.Popen(["python", "games\\rock_paper_scissors\\rock_paper_scissors.py"]).wait()
    root.deiconify()
    
def open_cookie_clicker():
    root.withdraw()
    subprocess.Popen(["python", "games\\cookie_clicker\\cookie_clicker.py"]).wait()
    root.deiconify()
    

# Create main window
root = tk.Tk()
root.title("GameHub")
root.geometry("500x600")
root.configure(bg="#2C2F33")

# Styling
button_style = {
    "font": ("Arial", 12, "bold"),
    "fg": "#ffffff",
    "bg": "#7289DA",
    "activebackground": "#5b6eae",
    "activeforeground": "#ffffff",
    "width": 20,
    "height": 2,
    "bd": 0
}

exit_button_style = button_style.copy()
exit_button_style["bg"] = "#ff4747"
exit_button_style["activebackground"] = "#c43838"

# Title Label
label = tk.Label(root, text="🎮 Welcome to GameHub 🎮", font=("Arial", 16, "bold"), fg="white", bg="#2C2F33")
label.pack(pady=20)

# Button Container Frame
frame = tk.Frame(root, bg="#2C2F33")
frame.pack(pady=10)

# Buttons to launch games
btn_game1 = tk.Button(frame, text="Simple Shooter", command=open_simple_shooter, **button_style)
btn_game1.pack(pady=10)

btn_game2 = tk.Button(frame, text="Guess The Number", command=open_guess_the_number, **button_style)
btn_game2.pack(pady=10)

btn_game3 = tk.Button(frame, text="Dino Game", command=open_dino_game, **button_style)
btn_game3.pack(pady=10)

btn_game4 = tk.Button(frame, text="Rock, Paper & Scissors", command=open_rock_paper_scissors, **button_style)
btn_game4.pack(pady=10)

btn_game5 = tk.Button(frame, text="Cookie Clicker", command=open_cookie_clicker, **button_style)
btn_game5.pack(pady=10)

# Exit Button
btn_exit = tk.Button(root, text="Exit", command=root.quit, **exit_button_style)
btn_exit.pack(pady=20)

# Run the Tkinter loop
root.mainloop()