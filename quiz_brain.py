class QuizBrain:

    def __init__(self, q_list, max_questions):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.max_questions = max_questions

    def still_has_questions(self):
        return self.question_number < len(self.question_list) and self.question_number < self.max_questions

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer_choices = current_question.choices
        print(f"Q.{self.question_number}: {current_question.text}")
        for i, choice in enumerate(answer_choices):
            print(f"{i+1}. {choice}")
        user_answer = input("Enter your answer (1-4): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        user_answer = int(user_answer) - 1  
        if user_answer == self.question_list[self.question_number-1].choices.index(correct_answer):
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")