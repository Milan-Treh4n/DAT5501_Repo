import json
import os
import random
from datetime import date
from quiz_questions.sport import quiz_questions_sport
from quiz_questions.science import quiz_questions_science
from quiz_questions.history import quiz_questions_history
from quiz_questions.general import quiz_questions_general

# Combine all themes
all_quiz_questions = {
    "sport": quiz_questions_sport,
    "science": quiz_questions_science,
    "history": quiz_questions_history,
    "general": quiz_questions_general
}

# File to save daily progress
progress_file = "daily_progress.json"

# Load previous progress if exists
if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        progress = json.load(f)
else:
    progress = {}

today = str(date.today())

if progress.get("last_played") == today:
    print("You have already completed today's Daily Challenge!")
    print(f"Score: {progress.get('score')}/10")
    exit(0)

# Select 10 random questions from all themes and difficulties
selected_questions = []
for _ in range(10):
    theme = random.choice(list(all_quiz_questions.keys()))
    difficulty = random.choice(list(all_quiz_questions[theme].keys()))
    question, answers = random.choice(all_quiz_questions[theme][difficulty])
    selected_questions.append((question, answers))

# Normalize function
def normalize(s):
    return "".join(s.lower().strip().split())

# Run the quiz
score = 0
for i, (question, answers) in enumerate(selected_questions, 1):
    print(f"\nQuestion {i}: {question}")
    user_answer = input("Your answer: ").strip()
    user_norm = normalize(user_answer)
    acceptable = [normalize(a) for a in answers]
    if user_norm in acceptable:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Not quite. Correct answer: {', '.join(answers)}")

# Save progress
progress = {
    "last_played": today,
    "score": score,
    "questions_answered": [q for q, _ in selected_questions]
}

with open(progress_file, "w") as f:
    json.dump(progress, f, indent=4)

print(f"\nDaily Challenge complete! Your score: {score}/10")
