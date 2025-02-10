import random
import tkinter as tk
import pygame
import time


# Initialize Pygame mixer
pygame.mixer.init()


def start_game():
    global number_to_guess, text_entry, submit_btn
    
    # Delete the Start button and display the game prompt
    start_btn.destroy()
    
    # Adjust label text
    label_prompt.configure(text="Guess a number from 1-100.")
    
    # Create text entry widget for player's guess
    text_entry = tk.Entry(root, font=("Arial", 12))
    text_entry.grid(row=2, pady=10)
    
    # Submit button to validate the guess
    submit_btn = tk.Button(root, text="Submit", command=validate_guess, font=("Arial", 12))
    submit_btn.grid(row=3, pady=10)
    
    # Keep the Exit button in place
    btn_exit.grid(row=4, pady=10)
    
    # Generate a random number between 1 and 100
    number_to_guess = random.choice(range(1, 101))


def validate_guess():
    global number_to_guess, text_entry
    
    try:
        # Get the player's guess
        player_guess = int(text_entry.get())
    except ValueError:
        label_prompt.configure(text="You need to input an integer number!")
    else:
        # Check if the guess is valid
        if 1 <= player_guess <= 100:
            if player_guess > number_to_guess:
                label_prompt.configure(text="Your number is too high!")
            elif player_guess < number_to_guess:
                label_prompt.configure(text="Your number is too low!")
            else:
                play_victory_sound()
                label_prompt.configure(text="You guessed the number!")
                submit_btn.configure(text="Play Again", command=play_again)
        else:
            label_prompt.configure(text="The number must be from 1-100!")
            

def play_again():
    submit_btn.destroy()
    start_game()


def play_music():
    pygame.mixer.music.load("games\\guess_the_number\\vibe_mountain.mp3")
    pygame.mixer.music.play(loops=-1)
    

def play_victory_sound():
    pygame.mixer.Sound("games\\guess_the_number\\coin_sound.mp3").play()
    

def exit_game():
    pygame.mixer.music.stop()
    root.quit()


def create_game_window():
    global root, label_prompt, start_btn, btn_exit
    
    # Create the Tkinter window
    root = tk.Tk()
    root.title("Guess The Number")
    root.geometry("600x300")
    
    # Configure the grid to center elements
    root.columnconfigure(0, weight=1)
    root.rowconfigure(2, weight=1)
    
    # Title Label
    label = tk.Label(root, text="Guess The Number", font=("Arial", 14))
    label.grid(row=0, pady=10)
    
    # Prompt text
    label_prompt = tk.Label(root, text="Press Start to play the game.", font=("Arial", 12))
    label_prompt.grid(row=1, pady=10)
    
    # Start button to initiate the game
    start_btn = tk.Button(root, text="Start", command=start_game, font=("Arial", 12))
    start_btn.grid(row=2, pady=10)
    
    # Exit button to close the game
    btn_exit = tk.Button(root, text="Exit", command=exit_game, font=("Arial", 12))
    btn_exit.grid(row=3, pady=10)


def main():
    play_music()
    create_game_window()
    root.mainloop()


if __name__ == "__main__":
    main()