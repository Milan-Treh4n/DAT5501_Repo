import random

# Questions database by theme and difficulty
quiz_questions = {
    "sport": {
        "easy": [
            "How many players are on a football team on the field?",
            "Which sport uses a shuttlecock?",
            "In basketball, how many points is a free throw worth?",
            "Which sport is known as 'the king of sports'?",
            "In tennis, what is the term for a score of zero?",
            "How many bases are there in baseball?",
            "Which country won the 2018 FIFA World Cup?",
            "What sport uses a puck?",
            "In which sport can you get a 'hole-in-one'?",
            "How long is an Olympic swimming pool?",
            
        ],
        "medium": [
            
        ],
        "hard": [
            
        ],
        "challenge": [
            
        ]
    },
    "science": {
        "easy": [
            "What planet is known as the Red Planet?",
            "What is H2O commonly called?",
            "Which gas do plants absorb from the atmosphere?",
            # Add more...
        ]
    },
    # Add other themes like history, general, music...
}

# Ask user for difficulty and theme
difficulty = input("Choose difficulty (easy, medium, hard, challenge): ").strip().lower()
theme = input("Choose a theme (sport, science, history, general): ").strip().lower()

# Validate input
if theme not in quiz_questions:
    print("Invalid theme")
    exit(1)
if difficulty not in quiz_questions[theme]:
    print("Invalid difficulty")
    exit(1)

# Select a random question
question = random.choice(quiz_questions[theme][difficulty])
print("Your question:")
print(question)



    