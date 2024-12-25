import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# File paths
QUESTIONS_FILE = r"C:\Users\Asus\Music\getting started\QUIZ_APPLICATION\questions.txt"
SCORES_FILE = r"C:\Users\Asus\Music\getting started\QUIZ_APPLICATION\scores.txt"

# Function to load questions from file
def load_questions(file_path):
    questions = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 6:  # Ensure proper question format
                    questions.append({
                        "question": parts[0],
                        "options": parts[1:5],
                        "answer": parts[5].upper()
                    })
    except FileNotFoundError:
        print(Fore.RED + f"Error: {file_path} not found.")
    return questions

# Function to save scores
def save_score(file_path, name, score, total):
    with open(file_path, "a") as file:
        file.write(f"{name},{score}/{total}\n")

# Function to display leaderboard
def display_leaderboard(file_path):
    print(Fore.CYAN + "\nLeaderboard:")
    try:
        with open(file_path, "r") as file:
            scores = [line.strip().split(",") for line in file.readlines()]
            scores = sorted(scores, key=lambda x: int(x[1].split("/")[0]), reverse=True)
            print(Fore.YELLOW + f"{'Rank':<5}{'Name':<20}{'Score'}")
            for rank, (name, score) in enumerate(scores, start=1):
                print(Fore.GREEN + f"{rank:<5}{name:<20}{score}")
    except FileNotFoundError:
        print(Fore.RED + f"Error: {file_path} not found.")
    except ValueError:
        print(Fore.RED + "Error: Scores file contains invalid data.")

# Quiz Application
def quiz_application():
    print(Fore.CYAN + "Welcome to the Quiz Application!")
    print(Fore.YELLOW + "Rules:")
    print("- Each question has 4 options.")
    print("- Enter the option (A, B, C, D) as your answer.")
    input(Fore.CYAN + "Press Enter to Start!\n")

    questions = load_questions(QUESTIONS_FILE)
    if not questions:
        print(Fore.RED + "No questions available. Please check the file.")
        return

    score = 0
    for i, q in enumerate(questions, start=1):
        print(Fore.BLUE + f"\nQuestion {i}: {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(Fore.GREEN + f"  {chr(64+idx)}. {option}")
        answer = input(Fore.YELLOW + "Your Answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print(Fore.GREEN + "Correct!\n")
            score += 1
        else:
            print(Fore.RED + f"Wrong! The correct answer was {q['answer']}.\n")

    print(Fore.CYAN + "\nQuiz Complete!")
    print(Fore.MAGENTA + f"Your Score: {score}/{len(questions)}")

    # Optionally save the score
    save = input(Fore.YELLOW + "Do you want to save your score? (y/n): ").strip().lower()
    if save == "y":
        name = input(Fore.CYAN + "Enter your name: ").strip()
        save_score(SCORES_FILE, name, score, len(questions))
        print(Fore.GREEN + f"Score recorded in {SCORES_FILE}")

    # Display leaderboard
    view_leaderboard = input(Fore.YELLOW + "Do you want to view the leaderboard? (y/n): ").strip().lower()
    if view_leaderboard == "y":
        display_leaderboard(SCORES_FILE)


if __name__ == "__main__":
    quiz_application()
