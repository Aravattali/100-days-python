from question_model import  Question
from data import  question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
	question_text = question["question"]
	question_answer = question["correct_answer"]
	new_question = Question(q_text= question_text , q_answer=question_answer)
	question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
	quiz.next_question()
print("you have completed the quiz")
print(f"your final score is {quiz.score}/ {quiz.question_number}")