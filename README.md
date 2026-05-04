# 🎯 Guess the Number (Python CLI Game)

A fun command-line game where the player tries to guess a randomly generated number within a limited number of attempts.

## 🚀 Features

- **Multiple difficulty levels** — Easy, Medium, and Hard
- **Limited attempts per game** — Each difficulty has a set number of guesses
- **Replay functionality** — Play as many rounds as you like
- **Input validation** — Handles non-numeric and out-of-range input gracefully
- **Clean modular design** — Logic is split across `config.py`, `game.py`, and `main.py`

## 📋 Difficulty Levels

| Level  | Range  | Attempts |
|--------|--------|----------|
| Easy   | 1–50   | 10       |
| Medium | 1–100  | 7        |
| Hard   | 1–200  | 5        |

## 🛠️ Installation

```bash
git clone https://github.com/aburr27/Guess-the-Number.git
cd Guess-the-Number
python main.py
```

## 🗂️ Project Structure

```
Guess-the-Number/
├── main.py    # Entry point — UI prompts and game loop
├── game.py    # Core game logic (target number, attempts, hints)
├── config.py  # Difficulty level configuration
└── README.md
```

## 🎮 How to Play

1. Run `python main.py`.
2. Choose a difficulty level (1 = Easy, 2 = Medium, 3 = Hard).
3. Enter guesses when prompted. After each guess you'll be told if your number is too low, too high, or correct.
4. Win by guessing the number before you run out of attempts.
5. When a round ends you'll be asked if you want to play again.