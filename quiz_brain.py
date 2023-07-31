class QuizBrain:
    def __init__(self, quiz_list):
        self.quiz_number = 0
        self.score = 0
        self.quiz_list = quiz_list

    def next_quiz(self):
        current_quiz = self.quiz_list[self.quiz_number]
        self.quiz_number += 1
        user_answer = input(
            f"Q.{self.quiz_number}: {current_quiz.text} (True/False): ")
        self.check_answer(user_answer, current_quiz.answer)

    def still_has_quiz(self):
        return self.quiz_number < len(self.quiz_list)

    def check_answer(self, user_answer, quiz_answer):
        if (user_answer.lower() == quiz_answer.lower()):
            self.score += 1
        else:
            print(f"You got it wrong. Correct answer is: {quiz_answer}")
        print(f"Score: {self.score}/{self.quiz_number}")
        print("\n")
