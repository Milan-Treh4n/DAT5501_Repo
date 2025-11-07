import random
import os
from PIL import Image

def show_image(filename):
    try:
        img_path = os.path.join(os.path.dirname(__file__), filename)
        Image.open(img_path).show()
    except Exception:
        pass

rounds_played = 0

while True:  # Keep playing until the user types exit
    user_choice = input("Enter your choice (rock, paper, scissors, exit): ").lower().strip()

    # Exit behavior depends on whether we've played any rounds yet
    if user_choice == 'exit':
        if rounds_played == 0:
            print("Maybe next time! Goodbye.")
        else:
            print("Thanks for playing! Goodbye.")
        break

    # Validate input
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors, or exit the game")
        continue

    # Valid round — increment counter
    rounds_played += 1

    # Computer plays
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    # Determine winner
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

    # Continue automatically
    print("Let's play again.")





    
