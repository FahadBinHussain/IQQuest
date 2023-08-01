class User:
    ALLOWED_USER_TYPES = ['school', 'college', 'university']

    def __init__(self, name, age, email, address, phone_number, user_type, category):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.user_type = user_type
        self.category = category
        self.quizzes_taken = 0
        self.total_score = 0
        self.highest_score = 0

    @staticmethod
    def validate_user_type(user_type):
        if user_type not in User.ALLOWED_USER_TYPES:
            raise ValueError("Invalid user_type. Allowed values are school, college, university.")

    def update_user_type(self, user_type):
        User.validate_user_type(user_type)
        self.user_type = user_type

    def increment_quizzes_taken(self):
        self.quizzes_taken += 1

    def update_total_score(self, score):
        self.total_score += score

        if score > self.highest_score:
            self.highest_score = score

    def calculate_average_score(self):
        if self.quizzes_taken > 0:
            return self.total_score / self.quizzes_taken
        else:
            return 0
        