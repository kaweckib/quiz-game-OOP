from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

if not quiz.still_has_questions():
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.current_score}/{quiz.question_number}")

