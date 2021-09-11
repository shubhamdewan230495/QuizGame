from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random
question_bank=[]
for item in question_data:
    question_bank.append(Question(item["text"],item["answer"]))
qb=QuizBrain(question_bank)
while qb.stillHaveQuestions():
    qb.retrievequestion()
    qb.question_number+=1
print(f'final score is {qb.score}/{len(qb.question_list)}')
