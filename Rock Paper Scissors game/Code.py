import random

# Ask user question
user_input = input("Do you want to play rock paper scissors? (yes/no): ").strip().lower()

if user_input == "yes":
    # Rock Paper Scissors Game
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    else:
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or

