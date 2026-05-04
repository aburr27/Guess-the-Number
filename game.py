import random


class Game:
    def __init__(self, difficulty: dict):
        self.min = difficulty["min"]
        self.max = difficulty["max"]
        self.max_attempts = difficulty["attempts"]
        self.target = random.randint(self.min, self.max)
        self.attempts_used = 0
        self.won = False

    def guess(self, number: int) -> str:
        """Process a guess and return a hint string.

        Returns one of: 'too_low', 'too_high', 'correct'.
        """
        self.attempts_used += 1
        if number < self.target:
            return "too_low"
        if number > self.target:
            return "too_high"
        self.won = True
        return "correct"

    @property
    def attempts_remaining(self) -> int:
        return self.max_attempts - self.attempts_used

    @property
    def is_over(self) -> bool:
        return self.won or self.attempts_remaining <= 0
