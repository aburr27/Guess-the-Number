import random  # Built-in module to generate random numbers
# This class handles all the game logic
class GuessTheNumberGame:
   # This runs when a new game is created
   def __init__(self, difficulty):
       self.difficulty = difficulty  # Store difficulty level chosen by user
       # Set max number and attempts based on difficulty
       self.max_number, self.max_attempts = self.set_difficulty()
       # Generate a random number between 1 and max_number
       self.secret_number = random.randint(1, self.max_number)
       self.attempts = 0  # Track how many guesses the player has made
   # Determines game settings based on difficulty
   def set_difficulty(self):
       if self.difficulty.lower() == "easy":
           return 50, 10  # Easier: smaller range, more attempts
       elif self.difficulty.lower() == "medium":
           return 100, 7
       elif self.difficulty.lower() == "hard":
           return 200, 5  # Harder: larger range, fewer attempts
       else:
           return 100, 7  # Default if input is invalid
   # Handles a player's guess
   def make_guess(self, guess):
       self.attempts += 1  # Increase attempt count every time user guesses
       # Compare guess to the secret number
       if guess == self.secret_number:
           return "You read my mind!"
       elif guess < self.secret_number:
           return "too low, go higher"
       else:
           return "too high, go lower"
   # Checks if player has used all attempts
   def is_game_over(self):
       return self.attempts >= self.max_attempts
