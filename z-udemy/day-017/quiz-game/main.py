from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text: str = question["text"]
    question_answer: str = question["answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)

# print(len(quiz.question_list))

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
