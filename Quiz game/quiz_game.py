import random
from quiz_questions.sport import quiz_questions_sport
from quiz_questions.science import quiz_questions_science
from quiz_questions.history import quiz_questions_history
from quiz_questions.general import quiz_questions_general


# Combine all themes into a single dictionary
all_quiz_questions = {
    "general": quiz_questions_general,
    "history": quiz_questions_history,
    "science": quiz_questions_science,
    "sport": quiz_questions_sport
}

def normalize(s):
    return "".join(s.lower().strip().split())

# Ask user for difficulty and theme
difficulty = input("Choose difficulty (easy, medium, hard, challenge): ").strip().lower()
theme = input("Choose a theme (sport, science, history, general): ").strip().lower()

# Validate input
if theme not in all_quiz_questions:
    print("Invalid theme")
    exit(1)
if difficulty not in all_quiz_questions[theme]:
    print("Invalid difficulty")
    exit(1)

# Select 10 random questions (unique) — no need to remove during the loop
selected_questions = random.sample(all_quiz_questions[theme][difficulty], 10)

score = 0

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


print(f"\nYour final score: {score}/10")


