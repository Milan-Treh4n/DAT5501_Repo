import random

def normalize(s):
    return "".join(s.lower().strip().split())

# Ask user for difficulty and theme
difficulty = input("Choose difficulty (easy, medium, hard, challenge): ").strip().lower()
theme = input("Choose a theme (sport, science, history, general): ").strip().lower()

# Basic validation to avoid KeyError later
if difficulty not in questions:
    print(f"Unknown difficulty '{difficulty}', defaulting to 'easy'.")
    difficulty = "easy"

if theme not in questions[difficulty]:
    print(f"Unknown theme '{theme}' for difficulty '{difficulty}', defaulting to first available theme.")
    theme = next(iter(questions[difficulty]))
# ...existing code...


def normalize(s):
    return "".join(s.lower().strip().split())

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

# Select 10 random questions
selected_questions = random.sample(quiz_questions[theme][difficulty], 10)

score = 0

# Ask each question inside the loop
for i, (question, answers) in enumerate(selected_questions, 1):
    print(f"\nQuestion {i}:")
    print(question)

    user_answer = input("Your answer: ").strip()
    user_norm = normalize(user_answer)

    acceptable = [normalize(a) for a in answers]

    if user_norm in acceptable:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Not quite. The correct answer is: {', '.join(answers)}")

# Final score
print(f"\nYour final score: {score}/10")



    