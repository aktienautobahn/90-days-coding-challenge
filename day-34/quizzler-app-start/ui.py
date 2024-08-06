from tkinter import *
import os
from quiz_brain import QuizBrain
import time

here = os.path.dirname(os.path.abspath(__file__))
right = os.path.join(here, 'images/true.png')
wrong = os.path.join(here, 'images/false.png')
THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizzlerInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(pady=20, bg=THEME_COLOR)


        #card back image
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        #load images

        self.right_img = PhotoImage(file=right)
        self.wrong_img = PhotoImage(file=wrong)
        
        #canvas_image = canvas.create_image(150, 125, image=card_front_img)
        self.question_text = self.canvas.create_text(150, 125, 
                                                    text="question", 
                                                    fill=THEME_COLOR, 
                                                    font=(FONT_NAME, 20, "italic"),
                                                    width=280)
        self.canvas.grid(padx=20, pady=50,column=0, row=1, columnspan=2)

         
        #score
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        #buttons
        self.right_button = Button(image=self.right_img, highlightbackground=THEME_COLOR, highlightthickness=0, command=self.button_true)
        self.right_button.grid(column=0,row=2)

        self.wrong_button = Button(image=self.wrong_img, highlightbackground=THEME_COLOR, highlightthickness=0, command=self.button_wrong)
        self.wrong_button.grid(column=1,row=2)

        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def button_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        score_text = f"Score: {self.quiz.score}"
        self.score.config(text=score_text)
        self.score.update()
        self.window.update()
        self.get_next_question()

    def button_wrong(self):
        is_right = self.quiz.check_answer("False")
        score_text = f"Score: {self.quiz.score}"
        self.score.config(text=score_text)
        self.score.update()
        self.window.update()
        self.give_feedback(is_right)

        self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.change_canvas_color("green")
        else:
            self.change_canvas_color("red")

    def change_canvas_color(self,color):
        self.canvas.config(bg=color)
        self.canvas.update() # Force canvas to update
        self.window.after(ms=1000)
        self.canvas.config(bg="white")
