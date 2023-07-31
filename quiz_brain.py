class QuizBrain:
    def __init__(self, quiz_list):
        self.quiz_number = 0
        self.quiz_list = quiz_list

    def next_quiz(self):
        current_quiz = self.quiz_list[self.quiz_number]
        return input(f"Q.{self.quiz_number}: {current_quiz.text} (True/False): ")
