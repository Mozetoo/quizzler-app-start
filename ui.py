THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
from tkinter import *
import html
from quiz_brain import *


class QuizUI:
    def __init__(self, quizbrain: QuizBrain):
        self.user_answer = None
        self.window = Tk()
        self.quiz = quizbrain
        self.start()
        self.value()

    def start(self):
        self.Num = 0
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR)
        self.window.configure(padx=20, pady=20)
        self.score = Label(text=f"Score : {self.Num}", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)
        self.question_box = Canvas(width=300, height=250, bg="white")
        self.tme = self.question_box.create_text(150, 125, text="", fill=THEME_COLOR, width=280)
        self.question_box.grid(row=1, column=0, columnspan=2, pady=50)
        self.tick_image = PhotoImage(file="images/true.png")
        self.tick = Button(image=self.tick_image, highlightthickness=0, bg=THEME_COLOR, command=self.answer)
        self.tick.grid(row=2, column=0, rowspan=2)

        self.cross_image = PhotoImage(file="images/false.png")
        self.cross = Button(image=self.cross_image, highlightthickness=0, bg=THEME_COLOR, command=self.wrong)
        self.cross.grid(row=2, column=1, rowspan=2)
        self.value()
        self.window.mainloop()

    def value(self):
        self.question_box.config(bg="white")
        if self.quiz.still_has_questions():
            text = self.quiz.next_question()
            self.question_box.itemconfig(self.tme, text=text)
        else:
            self.question_box.itemconfig(self.tme, text=f"You have reached the end of the quiz your final score is {self.quiz.score} ")
            self.cross.config(state="disabled")
            self.tick.config(state="disabled")


    def answer(self):
        is_right = self.quiz.check_answer(str(True))
        self.feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer(str(False))
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.question_box.config( bg="green")
            self.Num = self.quiz.score
            self.score.config(text=f"Score : {self.Num}")
        else:
            self.question_box.config(bg="red")
        self.window.after(1000, self.value)
