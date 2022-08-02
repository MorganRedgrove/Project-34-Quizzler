THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import *


class QuizInterface:
    def __init__(self):
        self.quiz = QuizBrain

        self.window = Tk()
        self.window.title(f"Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreboard = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.scoreboard.grid(column=2, row =1, padx=20, pady=20)

        self.card = Canvas(width=300, height=250, bg="white")
        self.question_text = self.card.create_text(
            150,
            125,
            text="",
            font=("Ariel",20,"italic"),
            fill=THEME_COLOR,
            width=280
        )
        self.card.grid(column=1, row=2, columnspan=2, padx=20, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_img)
        self.button_true.grid(column=1, row=3, padx=20, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_img)
        self.button_false.grid(column=2, row=3, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.card.itemconfig(self.question_text, text=q_text)


