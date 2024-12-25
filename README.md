Quiz Application
Description
The Quiz Application is a console-based Python application that allows users to take a quiz consisting of multiple-choice questions. The questions are loaded from a file, and at the end of the quiz, the user's score is displayed. Optionally, the application can store the user's performance data in a leaderboard file. The app also includes features to view the leaderboard and save scores for future reference.

This project is a simple start, and there are plans to enhance it with more features like timed quizzes, advanced question types, and more.

Features
Multiple-choice quiz questions with 4 options per question.
Display of correct or incorrect answers immediately after each question.
User score at the end of the quiz.
Option to save user scores to a leaderboard (scores.txt).
Display of a leaderboard showing the highest scores.
Colorful and user-friendly console interface using the colorama library.
Requirements
Python 3.x
colorama library for colored output
Installing colorama
To install the colorama library, use the following command:

bash
Copy code
pip install colorama
Files
1. questions.txt
This file contains the quiz questions, options, and the correct answer. The format is:

plaintext
Copy code
Question, Option A, Option B, Option C, Option D, Correct Answer
Example:

plaintext
Copy code
What is the capital of France?,Berlin,Madrid,Paris,Rome,C
Who developed the theory of relativity?,Isaac Newton,Albert Einstein,Nikola Tesla,Marie Curie,B
2. scores.txt
This file stores user scores in the format:

plaintext
Copy code
User Name, Score
Example:

plaintext
Copy code
John Doe,4/5
Alice,5/5
Note:
The questions.txt file should be in the same directory as the application script for the quiz to load questions correctly.
The scores.txt file will store user scores, and if the file does not exist, it will be created automatically.
How to Run the Application
Prepare the Questions File: Ensure that you have a questions.txt file containing the questions and answers in the format described above.

Run the Script: To start the quiz, simply run the Python script.

bash
Copy code
python quiz_application.py
Follow the Prompts:

The application will show a welcome message and the quiz rules.
The user will be asked to answer multiple-choice questions (A, B, C, D).
After answering all questions, the user's score will be displayed.
Optionally, users can choose to save their score and view the leaderboard.
Leaderboard: After completing the quiz, you can view the leaderboard to see top scores. Scores are saved to the scores.txt file, and the leaderboard is displayed in descending order of score.

Future Improvements
This is just the beginning, and several enhancements can be added, such as:

Timed Quiz: Implement a timer for each question to make the quiz more challenging.
Question Difficulty Levels: Add support for easy, medium, and hard questions.
Question Randomization: Randomize the order of questions and options to avoid repetition.
GUI Version: Create a graphical user interface (GUI) version of the quiz for better user experience.
Leaderboard Enhancements: Allow for better handling of high scores and display the rank for users.
License
This project is open-source and can be freely used and modified. Contributions are welcome!
