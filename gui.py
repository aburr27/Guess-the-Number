import tkinter as tk
from tkinter import messagebox
from game import GuessTheNumberGame  # Reuse your existing game logic

# This class controls the entire GUI application
class GuessTheNumberGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Guess The Number 🎯")
        self.root.geometry("400x300")

        self.game = None  # Will hold the game instance

        self.create_start_screen()

    # ---------------------------
    # START SCREEN (Choose difficulty)
    # ---------------------------
    def create_start_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="🎮 Guess The Number", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Choose Difficulty:").pack()

        # Buttons for difficulty levels
        tk.Button(self.root, text="Easy", command=lambda: self.start_game("easy")).pack(pady=5)
        tk.Button(self.root, text="Medium", command=lambda: self.start_game("medium")).pack(pady=5)
        tk.Button(self.root, text="Hard", command=lambda: self.start_game("hard")).pack(pady=5)

    # ---------------------------
    # START GAME
    # ---------------------------
    def start_game(self, difficulty):
        # Create new game instance
        self.game = GuessTheNumberGame(difficulty)

        self.clear_screen()

        # Display instructions
        self.info_label = tk.Label(
            self.root,
            text=f"Guess a number between 1 and {self.game.max_number}"
        )
        self.info_label.pack(pady=10)

        # Entry box for user input
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        # Submit button
        tk.Button(self.root, text="Submit Guess", command=self.submit_guess).pack(pady=5)

        # Feedback label (too high / too low)
        self.feedback_label = tk.Label(self.root, text="")
        self.feedback_label.pack(pady=10)

        # Attempts remaining
        self.attempts_label = tk.Label(
            self.root,
            text=f"Attempts left: {self.game.max_attempts}"
        )
        self.attempts_label.pack()

    # ---------------------------
    # HANDLE GUESS
    # ---------------------------
    def submit_guess(self):
        guess = self.entry.get()

        # Validate input
        if not guess.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        guess = int(guess)

        # Get result from game logic
        result = self.game.make_guess(guess)

        # Update attempts label
        remaining = self.game.max_attempts - self.game.attempts
        self.attempts_label.config(text=f"Attempts left: {remaining}")

        # Handle result cases
        if result == "correct":
            messagebox.showinfo("🎉 जीत!", f"You guessed it in {self.game.attempts} attempts!")
            self.create_start_screen()

        elif result == "too low":
            self.feedback_label.config(text="⬆️ Too Low!")

        else:
            self.feedback_label.config(text="⬇️ Too High!")

        # Check if game over
        if self.game.is_game_over() and result != "correct":
            messagebox.showinfo("Game Over", f"The number was {self.game.secret_number}")
            self.create_start_screen()

        # Clear input box after each guess
        self.entry.delete(0, tk.END)

    # ---------------------------
    # CLEAR SCREEN HELPER
    # ---------------------------
    def clear_screen(self):
        # Remove all widgets from window
        for widget in self.root.winfo_children():
            widget.destroy()


# ---------------------------
# RUN THE APP
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()  # Create main window
    app = GuessTheNumberGUI(root)  # Start app
    root.mainloop()  # Keep window running