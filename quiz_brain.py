class QuizBrain:
    def __init__(self, quiz_list):
        self.quiz_number = 0
        self.quiz_list = quiz_list

    def next_quiz(self):
        current_quiz = self.quiz_list[self.quiz_number]
        self.quiz_number += 1
        return input(f"Q.{self.quiz_number}: {current_quiz.text} (True/False): ")

    def still_has_quiz(self):
        return self.quiz_number < len(self.quiz_list)

    # def check_answer(self, answer):
    #     if(answer == ):
