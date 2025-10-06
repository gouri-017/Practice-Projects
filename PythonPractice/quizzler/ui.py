from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#006A71"
FONT = ('Arial', 20, 'italic')

class Ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.text =  Canvas.create_text(self.canvas,150,120, text="here will be the question",
                                        width=280,font=FONT,)
        self.canvas.grid(row= 1, column=0,columnspan = 2,pady = 50)
        self.score = Label(text='Score:0',bg=THEME_COLOR,fg="white",font =('sans-serif',15,'italic'))
        self.score.grid(row= 0, column=1)


        tick_img = PhotoImage(file='true.png')
        self.tick_button = Button(image=tick_img, highlightthickness=0, command=self.tick_button)
        self.tick_button.grid(row =2,column= 0)

        cross_img = PhotoImage(file='false.png')
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.cross_button)
        self.cross_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()


    def tick_button(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def cross_button(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score.config(text=f"Score :{self.quiz.score}")
        if self.quiz.still_has_questions():
                q_text = self.quiz.next_question()
                self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the Quiz.")
            self.tick_button.config(state='disabled')
            self.cross_button.config(state='disabled')

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)




