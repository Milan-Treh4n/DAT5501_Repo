import random
import string
import hashlib

# Ask the user wahat difficulty level they want
difficulty = input("Choose a difficulty level (easy, medium, hard, challenge): ").strip().lower()

# Set parameters based on difficulty level
if difficulty == "easy":
    length = 10
    charset = string.ascii_lowercase
elif difficulty == "medium":
    length = 10
    charset = string.ascii_letters + string.digits
elif difficulty == "hard":
    length = 10
    charset = string.ascii_letters + string.digits + string.punctuation
elif difficulty == "challenge":
    length = 15
    charset = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid difficulty level. Please choose from easy, medium, hard, or challenge.")
    exit(1)

    