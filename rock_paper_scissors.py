import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        self.choices = ['Rock', 'Paper', 'Scissors']
        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(master, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack()

        self.score_label = tk.Label(master, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        for choice in self.choices:
            button = tk.Button(self.button_frame, text=choice, width=10, command=lambda c=choice: self.play(c))
            button.pack(side=tk.LEFT, padx=10)

        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.check_winner(user_choice, computer_choice)

        if result == "win":
            self.user_score += 1
            result_text = "You Win!"
        elif result == "lose":
            self.computer_score += 1
            result_text = "You Lose!"
        else:
            result_text = "It's a Tie!"

        self.result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}.\n{result_text}")
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")

    def check_winner(self, user, comp):
        if user == comp:
            return "tie"
        elif (user == "Rock" and comp == "Scissors") or \
             (user == "Paper" and comp == "Rock") or \
             (user == "Scissors" and comp == "Paper"):
            return "win"
        else:
            return "lose"

    def reset_game(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Your Score: 0 | Computer Score: 0")

# Run the GUI app
root = tk.Tk()
game_app = RockPaperScissorsGame(root)
root.mainloop()
