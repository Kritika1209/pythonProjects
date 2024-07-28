from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank= []

for i in range(0, len(question_data)):
    question = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(question)

quiz= QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"Yoo've completed the Quiz!")
print(f"Your final score is {quiz.socre}/{len(question_data)}")