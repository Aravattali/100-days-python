# 🗺️ U.S. States Game in Python 🐍

This is a fun Python game that challenges users to name all 50 U.S. states. It uses the Turtle graphics module to display a blank U.S. map and writes correct guesses directly on the map.

## 🎮 How It Works

- The program displays a blank map of the U.S.
- The player is prompted to guess state names one by one.
- If the guess is correct, the state name appears on the map at the correct coordinates.
- Typing `"Exit"` ends the game and generates a CSV file `States_to_learn.csv` with all the states the player missed.

## 🧠 Skills Used

- Python turtle graphics
- File handling with `pandas`
- Basic data filtering
- GUI input with `Screen.textinput()`

## 🗂️ Files Included

- `main.py` - Main game logic
- `50_states.csv` - Contains `state`, `x`, `y` coordinates
- `blank_states_img.gif` - The map of the U.S. to display
- `States_to_learn.csv` - Automatically generated file with states the player missed
- `README.md` - This file!

## 📦 Requirements

- Python 3.x
- `pandas` library

Install with:

```bash
pip install pandas
