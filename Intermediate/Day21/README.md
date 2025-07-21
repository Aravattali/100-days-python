# 🐍 Snake Game – Turtle Module Project

Welcome to the classic **Snake Game** built with Python and the `turtle` graphics module! This project is part of the #100DaysOfCode challenge – Day 24 🎯

## 🎮 Gameplay Features

- Move the snake using the arrow keys (Up, Down, Left, Right)
- Eat the blue food to grow the snake
- Score increases with each bite
- Collision detection with:
  - Walls ➡ triggers reset
  - Tail ➡ triggers reset
- Scoreboard displays current score and high score
- High score is saved across sessions using a `.txt` file

## 📁 Project Structure

SnakeGame/
│
├── main.py # Main game loop
├── snake.py # Snake class (movement, collision, growth)
├── food.py # Food class (random position, appearance)
├── scoreboard.py # Scoreboard class (score logic, file handling)
├── data.txt # Stores high score
├── README.md # You're here!

markdown
Copy
Edit

## 🚀 How to Run

1. Make sure you have Python installed (3.x recommended)
2. Clone or download this repository
3. Run the game:

```bash
python3 main.py