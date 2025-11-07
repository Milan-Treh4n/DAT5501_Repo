# ...existing code...
import random
import os
from PIL import Image

def show_image(filename):
    try:
        img_path = os.path.join(os.path.dirname(__file__), filename)
        Image.open(img_path).show()
    except Exception:
        pass

while True:  # Loops the entire game until the user decides to quit
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()

    # Validate user input
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Generate computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        show_image("rock_win.png")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        show_image("paper_win.png")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        show_image("scissors_win.png")
    else:
        print("Computer wins!")
        show_image("computer_win.png")
        continue

    # Ask user if they would like to continue playing
    play_again = input("Do you want to play the game? (yes/no): ").lower().strip()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        exit()
    else:
        print("Great! Let's play again.")
        continue


    
