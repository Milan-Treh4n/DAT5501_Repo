import random
import os
from PIL import Image
# Ask the user for their choice
user_choice = input("Enter your choice (rock, paper, scissors): ").lower() 

# Validate user input
if user_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice! Please choose rock, paper, or scissors.")
    exit()

# Generate computer choice
computer_choice = random.choice(['rock', 'paper', 'scissors'])
print(f"Computer chose: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors"):
    print("You win!")
    img_path = os.path.join(os.path.dirname(__file__), "rock_win.png")
    Image.open(img_path).show()
elif (user_choice == "paper" and computer_choice == "rock"):
    print("You win!")
    img_path = os.path.join(os.path.dirname(__file__), "paper_win.png")
    Image.open(img_path).show()
elif (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
    img_path = os.path.join(os.path.dirname(__file__), "scissors_win.png")
    Image.open(img_path).show()
else:
    print("Computer wins!")
    img_path = os.path.join(os.path.dirname(__file__), "computer_win.png")
    Image.open(img_path).show()