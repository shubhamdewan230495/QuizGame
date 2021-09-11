class QuizBrain:
    def __init__(self,question_bank):
        self.score=0
        self.question_number=0
        self.question_list=question_bank
    def retrievequestion(self):
        self.answer=input(f"Q:{self.question_number+1} {self.question_list[self.question_number].text} (True/False)")
        self.result=self.checkAnswer(self.answer,self.question_list[self.question_number].answer)
        if self.result==True:
            self.score+=1
            print('answer is correct')
            print(f'your current score is {self.score}')
            print('\n')
        else:
            print("you're wrong")

    def stillHaveQuestions(self):
        return self.question_number<len(self.question_list)

    def checkAnswer(self,actual,expected):
        return actual.lower()==expected.lower()
