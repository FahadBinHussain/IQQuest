import requests
import yaml
from user_model import User
from question_model import Question
from quiz_brain import QuizBrain

# Fetch trivia questions from the Open Trivia Database API
response = requests.get("https://opentdb.com/api.php?amount=50&category=18&type=multiple")
response.raise_for_status()  # Raise an exception if request fails
question_data = response.json()["results"]

try:
    # Try to open the existing users.yml file
    with open('users.yml', 'r') as file:
        user_data = yaml.safe_load(file)
except FileNotFoundError:
    # If the file doesn't exist, create an empty user_data dictionary
    user_data = {'users': []}

while True:
    # Ask the user for their information
    name = input("Enter your name: ")
    if name.lower() == 'exit':
        break

    # Ask the user for their information
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")

    # Validate and prompt for user type until a valid value is provided
    while True:
        user_type = input("Enter your user type: ")
        try:
            User.validate_user_type(user_type)
            break
        except ValueError as e:
            print(e)

    category = input("Enter your category: ")

    # Create a new user dictionary
    new_user = {
        'name': name,
        'age': age,
        'email': email,
        'address': address,
        'phone_number': phone_number,
        'user_type': user_type,
        'category': category
    }

    # Append the new user dictionary to the existing user data
    user_data['users'].append(new_user)

    # Save the updated user information back to the YAML file
    with open('users.yml', 'w') as file:
        yaml.dump(user_data, file)

    user = User(name, age, email, address, phone_number, user_type, category)

    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        incorrect_answers = question["incorrect_answers"]
        all_answers = incorrect_answers + [question_answer]
        new_question = Question(question_text, all_answers, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank, max_questions=2)

    while quiz.still_has_questions():
        quiz.next_question()

        user.update_total_score(quiz.score)

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
