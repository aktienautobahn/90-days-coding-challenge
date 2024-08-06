#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're end of the quiz
import random

class QuizBrane:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
    def still_has_question(self):
        return len(self.question_list) > self.question_number
    
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1      
        self.answer = input(f"Q.{self.question_number}: {self.current_question.text} (True or False)?: ").lower()

    
    #checking if the answer was correct
    def correct_answer(self):
        if self.answer == self.current_question.answer.lower():
            self.score += 1
            print(f"You got it right!\nThe correct answer was: {self.current_question.answer}\nYour current score is : {self.score}/{self.question_number}\n\n")
        else:
            print(f"Sorry mate, your answer is wrong!\nThe correct answer was: {self.current_question.answer}\nYour current score is : {self.score}/{self.question_number}\n\n")
    #checking if we're end of the quiz
#TODO: Timur