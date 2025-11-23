import json
import os
import random
from datetime import datetime, date
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

# Prevent replaying the same day
if progress.get("last_played") == today:
    print("You have already completed today's Daily Challenge!")
    print(f"Score: {progress.get('score')}/10")
    exit(0)

# Pick 10 questions from random themes + difficulties
selected_questions = []
for _ in range(10):
    theme = random.choice(list(all_quiz_questions.keys()))
    difficulty = random.choice(list(all_quiz_questions[theme].keys()))
    question, answers = random.choice(all_quiz_questions[theme][difficulty])
    selected_questions.append((question, answers))

# Normalise function
def normalise(s):
    return "".join(s.lower().strip().split())

# Run quiz
score = 0
answered_list = []

for i, (question, answers) in enumerate(selected_questions, 1):
    print(f"\nQuestion {i}: {question}")
    user_answer = input("Your answer: ").strip()
    user_norm = normalise(user_answer)
    acceptable = [normalise(a) for a in answers]

    correct = user_norm in acceptable

    if correct:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Not quite. Correct answer: {', '.join(answers)}")

    # store what user answered
    answered_list.append({
        "question": question,
        "user_answer": user_answer,
        "correct": correct
    })

    # Ensure no question is repeated
    selected_questions.remove((question, answers)) 

# Save progress to JSON
progress = {
    "last_played": today,
    "last_played_time": datetime.now().strftime("%H:%M:%S"),
    "score": score,
    "questions_answered": answered_list
}

with open(progress_file, "w") as f:
    json.dump(progress, f, indent=4)

print(f"\nDaily Challenge complete! Your score: {score}/10")
