# 🏓 Pong Game with Turtle Graphics

This is a classic Pong game recreated using Python's `turtle` module. It features two paddles, a ball, and a scoreboard to keep track of the players' scores.

---

## 📦 Features

- Two-player game:  
  - Player 1 (Left Paddle): Controls with `W` (up) and `S` (down)  
  - Player 2 (Right Paddle): Controls with `Up Arrow` and `Down Arrow`
- Ball movement with collision detection
- Scoreboard for both players
- Ball resets and score updates when a paddle misses

---

## 🧠 How It Works

The game uses four main components:

1. **`main.py`** – Contains the game loop and event listeners.
2. **`paddle.py`** – Contains the `Paddle` class for left and right paddles.
3. **`ball.py`** – Contains the `Ball` class that handles movement and collisions.
4. **`scoreboard.py`** – Contains the `Scoreboard` class for keeping track of scores.

---

## 🛠 Requirements

- Python 3.x
- No external libraries needed (only `turtle` module, which comes with Python)

---

## ▶️ How to Run

1. Make sure you have all the following files in the same directory:
   - `main.py`
   - `paddle.py`
   - `ball.py`
   - `scoreboard.py`

2. Run the game:

```bash
python main.py
