class QuizBrain:
    
    def __init__(self,  q_list):
        self.q_no=0
        self.question_list= q_list
        self.score=0

    def check_answer(self, user_ans, corr_ans):
        if user_ans == corr_ans:
            print("That is correct")

            self.score += 1
            print(f"Your Score is {self.score}/{self.q_no}")
        else:
            print("That is the wrong answer")
            print(f"The correct answer is {corr_ans}")
            print(f"Your score is {self.score}/{self.q_no}")
        
        print("\n")
    
    def next_question(self):
        curr_ques= self.question_list[self.q_no]
        ans= input(f"Q.{self.q_no+1}: {curr_ques.question}? (True/False) ")
        self.q_no += 1
        self.check_answer(ans, curr_ques.answer)
        
            
            
    def still_has_questions(self):
        if self.q_no< len(self.question_list):
            return True
        else:
            return False
        
  
   
        