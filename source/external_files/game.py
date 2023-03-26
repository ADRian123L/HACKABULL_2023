import tkinter as tk
import random

class BinaryConversionGame:
    def __init__(self, master):
        self.master = master
        self.level = 1
        self.setup_ui()

    def setup_ui(self) -> None:
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(padx=10, pady=10)

        # Question label
        self.question_label = tk.Label(self.main_frame, text="Decimal number:")
        self.question_label.grid(row=0, column=0, padx=5, pady=5)

        # Decimal number display
        self.decimal_var = tk.StringVar()
        self.decimal_label = tk.Label(self.main_frame, textvariable=self.decimal_var)
        self.decimal_label.grid(row=0, column=1, padx=5, pady=5)

        # User input entry
        self.input_entry = tk.Entry(self.main_frame)
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.input_entry.bind("<Return>", self.handle_input)

        # Submit button
        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.check_answer)
        self.submit_button.grid(row=2, column=0, padx=5, pady=5)

        # Feedback label
        self.feedback_var = tk.StringVar()
        self.feedback_label = tk.Label(self.main_frame, textvariable=self.feedback_var)
        self.feedback_label.grid(row=2, column=1, padx=5, pady=5)

        # Level label
        self.level_label = tk.Label(self.main_frame, text=f"Level: {self.level}")
        self.level_label.grid(row=3, column=0, padx=5, pady=5)

        self.new_question()
        self.update_display()

    def new_question(self) -> None:
        self.decimal_number = random.randint(1, 2 ** self.level)

    def update_display(self) -> None:
        self.decimal_var.set(self.decimal_number)
        self.input_entry.delete(0, tk.END)
        self.feedback_var.set("")

    def handle_input(self, event=None) -> None:
        user_input = self.input_entry.get()
        if user_input:
            self.check_answer()

    def reset_game(self) -> None:
        self.level += 1
        self.new_question()
        self.update_display()
        self.level_label.config(text=f"Level: {self.level}")

    def check_answer(self) -> None:
        user_input = self.input_entry.get()
        try:
            user_binary = int(user_input, 2)
            if user_binary == self.decimal_number:
                self.feedback_var.set("Correct!")
                self.reset_game()
            else:
                self.feedback_var.set("Incorrect. Try again.")
        except ValueError:
            self.feedback_var.set("Invalid input. Enter binary only.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Binary Conversion Game")
    game = BinaryConversionGame(root)
    root.mainloop()
