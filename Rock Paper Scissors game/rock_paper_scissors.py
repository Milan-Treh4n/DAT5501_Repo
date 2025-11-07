import random
import os
from PIL import Image
import matplotlib.pyplot as plt   # Added for reliable image display

def show_image(filename):
    try:
        img_path = os.path.join(os.path.dirname(__file__), filename)
        img = Image.open(img_path)

        # Display image in a Python window (works on any computer)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    except Exception:
        pass  # Silent fail if image missing

rounds_played = 0

while True:  # Keep playing until user confirms exit
    user_choice = input("Enter your choice (rock, paper, scissors, exit): ").lower().strip()

    if user_choice == 'exit':
        confirm = input("Are you sure you want to exit? (yes/no): ").lower().strip()
        if confirm == 'yes':
            print("Ok see you next time.")
            break
        else:
            print("Great! Let's play again.")
            continue

    # Validate input
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors, or exit the game")
        continue

    # Valid round
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

    print("Great! Let's play again.")






    
