🐢 Turtle Crossing Game
A fun arcade-style game built using Python and the Turtle graphics library. Help the turtle cross the road and reach the top safely while avoiding cars. With each level, the cars move faster!

🚀 Features
Turtle player controlled by the Up arrow key

Randomly generated cars with different colors and positions

Increasing difficulty with each level

Collision detection and game-over screen

Clean and modular object-oriented design

📂 Project Structure
bash
Copy
Edit
turtle-crossing/
│
├── main.py              # Main game loop
├── player.py            # Player (Turtle) class
├── car_manager.py       # Handles car creation and movement
├── scoreboard.py        # Displays level and Game Over
└── README.md            # Project description and instructions
📸 Gameplay Preview
You can include a screenshot or GIF here later

🎮 Controls
Press Up Arrow (↑) to move the turtle forward

🧠 How It Works
The game screen is set up with a Screen object.

A turtle is created as the player and moves upward when you press the Up arrow.

Cars spawn randomly on the right side and move to the left.

If a car collides with the player, the game ends.

When the turtle reaches the top, it returns to the start, and the game level increases, making cars move faster.

🛠 Requirements
Python 3.x

No external libraries needed other than the built-in turtle and random modules.

▶️ How to Run
Make sure you have Python installed.

Save all .py files (main.py, player.py, car_manager.py, scoreboard.py) in the same folder.

Run the main.py file:

bash
Copy
Edit
python main.py
👨‍💻 Author
Arafat Ali

