# Quiz Game

This folder contains a fun Python quiz game I created to practice coding and challenge myself with friends in a quiz society. It is written for beginners: open the script, run it in the terminal, and answer questions to see how the game works.

What’s included
- quiz_game.py — the main script to play the quiz.
- quiz_questions/ — folder containing theme files (sport.py, science.py, history.py, general.py) with all the questions and answers.
- Optional output: your score and feedback appear in the terminal while playing.

What the script does (short)
- quiz_game.py: asks the player to select a difficulty level and a quiz theme, presents 10 random questions, checks answers, and keeps score. It also gives feedback for correct and wrong answers.

How to run (macOS, minimal)
1. Open Terminal at the repository root.
2. (Optional but recommended) Create and activate a virtual environment:

# Daily Challenge

The Daily Challenge is a special quiz mode that gives you a mix of questions from all themes (sport, science, history, general) and all difficulty levels. You can play it once per day to test your knowledge and track your progress over time.

How it works:
- Each day, 10 random questions are selected from all available themes and difficulties.
- Your score and the questions you answered are saved in a file (`daily_progress.json`), so you can track your progress.
- You can only complete the Daily Challenge once per day. If you try again on the same day, the game will show your previous score.
- The goal is to get the highest score possible while learning and having fun with friends.

Suggested use:
- Play Daily Challenge regularly to practice and improve in all quiz themes.
- Compare your score with friends to see who has the best streak or highest score.
