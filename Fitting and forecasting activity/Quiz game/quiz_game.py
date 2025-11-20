import random
import string
import hashlib

# Ask the user what difficulty level they want
difficulty = input("Choose a difficulty level (easy, medium, hard, challenge): ").strip().lower()

# Ask the user what quiz theme they want
theme = input("Choose a quiz theme (sport,science, history, general): ").strip().lower()

# Validate the theme
if theme not in ["sport", "science", "history", "general"]:
    print("Invalid theme. Please choose from sport, science, history, or general.")
    exit(1)

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

    