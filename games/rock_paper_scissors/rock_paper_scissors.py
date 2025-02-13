import random
import tkinter as tk
import pygame


# Initialize Pygame mixer
pygame.mixer.init()

choices = ['r', 'p', 's']
bot_choice = None


def start_game():
    global bot_choice
    
    # Delete the Start button and display the game prompt
    start_btn.destroy()
    
    # Adjust label text
    label_prompt.configure(text="Choss either Rock, Paper or Scissors.")
    
    # Create buttons with lambda to correctly delay execution
    rock_btn = tk.Button(root, text="Rock", command=lambda: play_game('r'), font=("Arial", 12))
    rock_btn.grid(row=2, column=0, pady=10)
    
    paper_btn = tk.Button(root, text="Paper", command=lambda: play_game('p'), font=("Arial", 12))
    paper_btn.grid(row=2, column=1, pady=10)
    
    scissors_btn = tk.Button(root, text="Scissors", command=lambda: play_game('s'), font=("Arial", 12))
    scissors_btn.grid(row=2, column=2, pady=10)
    
    # Generate bot choice
    bot_choice = random.choice(choices)


def play_game(player_choice: str):    
    if player_choice == bot_choice:
        print("Tie")
        label_prompt.configure(text="It's a Tie!")
    elif player_choice == 'r' and bot_choice == 's':
        label_prompt.configure(text="You win!")
    elif player_choice == 'p' and bot_choice == 'r':
        label_prompt.configure(text="You win!")
    elif player_choice == 's' and bot_choice == 'p':
        label_prompt.configure(text="You win!")
    else:
        label_prompt.configure(text="Bot wins!")


def exit_game():
    pygame.mixer.music.stop()
    root.quit()


def create_game_window():
    global root, label_prompt, start_btn, btn_exit
    
    # Create the Tkinter window
    root = tk.Tk()
    root.title("Rock, Paper & Scissors")
    root.geometry("600x300")
    
    # Configure the grid to center elements
    root.columnconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    
    # Title Label
    label = tk.Label(root, text="Rock, Paper & Scissors", font=("Arial", 14))
    label.grid(row=0, column=1, pady=10)
    
    # Prompt text
    label_prompt = tk.Label(root, text="Press Start to play the game.", font=("Arial", 12))
    label_prompt.grid(row=1, column=1, pady=10)
    
    # Start button to initiate the game
    start_btn = tk.Button(root, text="Start", command=start_game, font=("Arial", 12))
    start_btn.grid(row=2, column=1, pady=10)
    
    # Exit button to close the game
    btn_exit = tk.Button(root, text="Exit", command=exit_game, font=("Arial", 12))
    btn_exit.grid(row=3, column=1, pady=10)


if __name__ == "__main__":
    create_game_window()
    root.mainloop()