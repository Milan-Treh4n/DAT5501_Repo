import random

# Questions database by theme and difficulty
quiz_questions = {
    "sport": {
        "easy": [
            ("How many players are on a football team on the field?", ["11", "eleven"]),
            ("Which sport uses a shuttlecock?", ["badminton"]),
            ("In basketball, how many points is a free throw worth?", ["1", "one"]),
            ("Which sport is known as 'the king of sports'?", ["football", "soccer"]),
            ("In tennis, what is the term for a score of zero?", ["love"]),
            ("How many bases are there in baseball?", ["4", "four"]),
            ("Which country won the 2018 FIFA World Cup?", ["france"]),
            ("What sport uses a puck?", ["ice hockey", "hockey"]),
            ("In which sport can you get a 'hole-in-one'?", ["golf"]),
            ("How long is an Olympic swimming pool?", ["50", "50m", "50 metres", "50 meters"]),
        ]
    }


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



    