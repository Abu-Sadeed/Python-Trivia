from question_model import Quiz
from data import question_data
from quiz_brain import QuizBrain

quizzes = []

for questions in question_data:
    quiz_text = questions["text"]
    quiz_answer = questions["answer"]
    new_quiz = Quiz(quiz_text, quiz_answer)
    quizzes.append(new_quiz)

quiz = QuizBrain(quizzes)

while quiz.still_has_quiz():
    answer = quiz.next_quiz()


print(answer)
