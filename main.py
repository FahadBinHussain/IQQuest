import requests
from question_model import Question
from quiz_brain import QuizBrain

# Fetch trivia questions from the Open Trivia Database API
response = requests.get("https://opentdb.com/api.php?amount=50&category=18&type=multiple")
response.raise_for_status()  # Raise an exception if request fails
question_data = response.json()["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    incorrect_answers = question["incorrect_answers"]
    all_answers = incorrect_answers + [question_answer]
    new_question = Question(question_text, all_answers, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank, max_questions=10)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
