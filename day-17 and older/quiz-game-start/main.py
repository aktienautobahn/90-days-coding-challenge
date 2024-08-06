from question_model import Question
from data import question_data
from quiz_brain import QuizBrane

question_bank = []

for question in question_data:
    question_bank.append(Question(q_text = question['text'], q_answer = question['answer']))



quiz_brain = QuizBrane(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()
    quiz_brain.correct_answer()

print("You have completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")