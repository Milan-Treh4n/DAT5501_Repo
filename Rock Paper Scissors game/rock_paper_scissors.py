import random
import base64
from io import BytesIO
from PIL import Image

# Import base64 dictionary
from base64_for_images import base64_variables as images

# Function to display image from base64
def show_image_from_base64(b64_string) -> None:
    try:
        image_data = base64.b64decode(b64_string)
        img = Image.open(BytesIO(image_data))
        img.show()
    except Exception as e:
        print("Image failed to display:", e)

rounds_played = 0

while True:  # Keep playing until user exits
    user_choice = input("Enter your choice (rock, paper, scissors, exit): ").lower().strip()

    if user_choice == 'exit':
        confirm = input("Are you sure you want to exit? (yes/no): ").lower().strip()
        if confirm == 'yes':
            print("Ok see you next time.")
            break
        else:
            print("Great! Let's play again.")
            continue

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors, or exit the game.")
        continue

    rounds_played += 1

    # Computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        show_image_from_base64(images[f"{user_choice}_win_b64"])

    else:
        print("Computer wins!")
        show_image_from_base64(images["computer_win_b64"])

    print("Let's play again.")









    
