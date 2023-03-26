import tkinter as tk

class MathQuizApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Base Conversion App")

        self.questions = ["What is 10 in base 2", "What is 5 / 2?", "What is 2 / 2"]
        self.answers = ["0", "1", "0"]
        self.levels = range(0, 3)
        self.current_level = 0
        self.current_question_index = 0

        self.build_ui()

    def build_ui(self) -> None:
        self.question_label = tk.Label(self, text=self.questions[self.current_question_index])
        self.question_label.pack(padx=20, pady=20)

        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(padx=20, pady=20)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(padx=20, pady=20)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.pack(padx=20, pady=20)

    def check_answer(self) -> None:
        answer = self.answer_entry.get()
        if answer == self.answers[self.current_question_index]:
            self.current_question_index += 1

            if self.current_question_index < len(self.questions):
                self.update_ui()
            else:
                self.reset()

    def level(self, condition: bool) -> None:
        """The function is used to increase the level of the quiz"""
        if condition:
            self.current_level += 1
        
    def append(self, level: int = 0) -> None:
        """"""
        for i in range(level):
            pass

        
    def update_ui(self):
        self.question_label.config(text=self.questions[self.current_question_index])
        self.answer_entry.delete(0, tk.END)

    def reset(self):
        self.current_question_index = 0
        self.update_ui()

if __name__ == "__main__":
    app = MathQuizApp()
    app.mainloop()
