# Import game logic and helper function
from game import GuessTheNumberGame
from utils import get_valid_number
# This function runs one full game session
def play():
   print("🎮 Welcome to Guess the Number!")
   # Ask user to choose difficulty
   difficulty = input("Choose difficulty (easy/medium/hard): ")
   # Create a new game instance
   game = GuessTheNumberGame(difficulty)
   # Display game rules based on difficulty
   print(f"\nI'm thinking of a number between 1 and {game.max_number}")
   print(f"You have {game.max_attempts} attempts.\n")
   # Loop until game ends
   while not game.is_game_over():
       # Get a valid number from user
       guess = get_valid_number("Enter your guess: ")
       # Check the result of the guess
       result = game.make_guess(guess)
       # Handle result outcomes
       if result == "correct":
           print(f"🎉 You got it in {game.attempts} attempts!")
           return  # End game if correct
       elif result == "too low":
           print("⬆️ Too low!")
       else:
           print("⬇️ Too high!")
       # Show remaining attempts
       print(f"Attempts left: {game.max_attempts - game.attempts}\n")
   # If loop ends, player ran out of attempts
   print(f"💀 Game Over! The number was {game.secret_number}")
# This controls replay functionality
def main():
   while True:
       play()  # Run the game
       # Ask if player wants to play again
       again = input("\nPlay again? (y/n): ").lower()
       if again != "y":
           print("👋 Thanks for playing!")
           break  # Exit loop and end program
# This ensures the script runs only when executed directly
if __name__ == "__main__":
   main()
