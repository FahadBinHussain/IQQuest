# IQQuest

This project is a Python-based quiz game that fetches trivia questions from the Open Trivia Database API and tests the user's knowledge of computer science.

# Dependencies

* requests

# How to Use

## Critical prerequisites to install

* run ```pip3 install -r requirements.txt```

You're all set.

## Run the script on the desktop

1. Open a terminal or command prompt

2. Navigate to the directory where you cloned the repository

3. Run `python3 main.py` to start the Quest!

## How the Quiz Game works

* This quiz game works by fetching trivia questions from the Open Trivia Database API and testing the user's knowledge of computer science.

* When the game starts, it makes an HTTP GET request to the Open Trivia Database API endpoint to fetch 50 multiple-choice trivia questions related to computer science. It then creates a `Question` object for each question, and a list of `Question` objects is passed to the `QuizBrain` class.

* The `QuizBrain` class keeps track of the user's score and the number of questions answered. It prompts the user to select an answer for each question and validates the answer using the `check_answer` method. If the user's answer is correct, the score is incremented. The `QuizBrain` class continues to prompt the user with questions until there are no questions left.

* At the end of the quiz, the user's score is displayed along with the number of questions answered.

* The code uses the `requests` library to make HTTP requests and the `json` library to parse the JSON response from the Open Trivia Database API. The `QuizBrain` and `Question` classes are defined in separate Python modules called `quiz_brain.py` and `question_model.py`, respectively. The `main.py` file imports these modules and creates an instance of the `QuizBrain` class to run the quiz game.
