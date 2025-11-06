import random
import PIL
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
    PIL.Image.open("rock_win.png").show()