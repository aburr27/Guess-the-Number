from config import DIFFICULTY_LEVELS
from game import Game


def get_difficulty() -> dict:
    """Prompt the player to choose a difficulty level."""
    print("\nSelect difficulty:")
    for key, level in DIFFICULTY_LEVELS.items():
        print(
            f"  {key}. {level['name']}  "
            f"(1–{level['max']}, {level['attempts']} attempts)"
        )
    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice in DIFFICULTY_LEVELS:
            return DIFFICULTY_LEVELS[choice]
        print("Invalid choice. Please enter 1, 2, or 3.")


def get_guess(min_val: int, max_val: int) -> int:
    """Prompt the player for a valid integer guess."""
    while True:
        raw = input(f"Enter your guess ({min_val}–{max_val}): ").strip()
        try:
            number = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if number < min_val or number > max_val:
            print(f"Please guess between {min_val} and {max_val}.")
            continue
        return number


def play_round(difficulty: dict) -> None:
    """Play a single round of the game."""
    game = Game(difficulty)
    level_name = difficulty["name"]
    print(
        f"\n🎯 {level_name} — Guess a number between "
        f"{game.min} and {game.max}. "
        f"You have {game.max_attempts} attempts."
    )

    while not game.is_over:
        print(f"  Attempts remaining: {game.attempts_remaining}")
        player_guess = get_guess(game.min, game.max)
        result = game.guess(player_guess)

        if result == "correct":
            print(
                f"✅ Correct! You guessed it in {game.attempts_used} "
                f"attempt{'s' if game.attempts_used != 1 else ''}."
            )
        elif result == "too_low":
            print("📉 Too low!")
        else:
            print("📈 Too high!")

    if not game.won:
        print(f"❌ Out of attempts! The number was {game.target}.")


def ask_replay() -> bool:
    """Ask the player if they want to play again."""
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def main() -> None:
    print("=" * 40)
    print("       🔢 Guess the Number! 🔢")
    print("=" * 40)

    while True:
        difficulty = get_difficulty()
        play_round(difficulty)
        if not ask_replay():
            break

    print("\nThanks for playing! Goodbye. 👋")


if __name__ == "__main__":
    main()
