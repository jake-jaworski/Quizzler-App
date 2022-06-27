from tkinter import *
from quiz_brain import QuizBrain
# from main import quiz

THEME_COLOR = "#375362"

class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, highlightbackground=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            150,
            width=275,
            text="placeholder",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_gif = PhotoImage(file="images/true.gif")
        self.true_button = Button(image=true_gif, command=self.user_clicked_true)
        self.true_button.grid(row=2, column=0)

        false_gif = PhotoImage(file="images/false.gif")
        self.false_button = Button(image=false_gif, command=self.user_clicked_false)
        self.false_button.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_t = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_t)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've completed the quiz. Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def user_clicked_true(self):
        correct_guess = self.quiz.check_answer("True")
        self.give_feedback(correct_guess)

    def user_clicked_false(self):
        correct_guess = self.quiz.check_answer("False")
        self.give_feedback(correct_guess)

    def give_feedback(self, guess):
        if guess:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_question)


