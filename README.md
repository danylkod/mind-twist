# Mind Twist: Words and Colors

Welcome to **Mind Twist: Words and Colors**, stranger! :)

This is fun and interactive game designed to challenge your focus and quick thinking! Test your ability to correctly identify words or colors under time pressure. Choose your preferred game mode and see how high you can score!

---

## Features

- **Three Game Modes**:
  - **Words**: Identify and type the word displayed.
  - **Colors**: Identify and type the color of the displayed word.
  - **Mix**: A randomized combination of both challenges.
- **Dynamic Gameplay**:
  - Tracks your score in real-time.
  - Automatically transitions between challenges.
- **High Score Tracker**:
  - Saves your highest score for each game mode.
  - Displays the highest scores in a separate window at the end of the game.

---

## How to Play

1. **Start the Game**:

   - Choose a mode by clicking on one of the buttons: **Words**, **Colors**, or **Mix**.
   - Press the `Q` key to start the game.

2. **Gameplay**:

   - Type the correct answer based on the game mode:
     - For **Words** mode: Type the word displayed on the screen.
     - For **Colors** mode: Type the color of the text displayed.
     - For **Mix** mode: Follow the instructions given for each round.
   - Press `Enter` after typing your answer to submit and move to the next challenge.

3. **Time Limit**:

   - You have **30 seconds** to score as many points as possible.

4. **End of Game**:
   - When time is up, a new window will display your highest scores for all modes.

---

## Installation and Requirements

### Prerequisites

- Python 3.7 or later
- `tkinter` (pre-installed with Python on most systems)

### Steps to Run

1. Clone or download this repository to your local machine.
2. Open a terminal in the project directory.
3. Run the following command to start the game:

```bash
python mind_twist.py
```

4. Enjoy the game!

---

## File structure

```bash
mind_twist.py # The main game file.
highest_scores.txt # Stores the highest scores for each game mode. This file will be created automatically after the first game.
```

---

## Key Bindings

- **Q**: Start the game.
- **Enter**: Submit your answer.

---

## Scoring System

- **Correct Answer**: +1 point.
- **Incorrect Answer**: No points are awarded.

The highest scores for each mode are saved and displayed at the end of the game.

---

## Credits

- Developed using **Python** and **Tkinter**.
- Inspired by Stroop effect cognitive psychology experiments.
