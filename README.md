# Python Quiz Game

This is a text-based quiz game implemented in Python using the `curses` library. The game features multiple levels with different types of arithmetic problems, including addition, subtraction, and division. The game has a built-in timer for each question, and the player can quit at any time by pressing the 'q' key.

## Features:
- **Multiple Levels**: 
  - Level 1: Two-digit addition
  - Level 2: Three-digit addition
  - Level 3: Two-digit subtraction
  - Level 4: Three-digit subtraction
  - Level 5: One-digit multiplication
  - Level 6: Two-digit multiplication
  - Level 7: Three-digit multiplication
  - Level 8: Two-digit division
- **Timed Questions**: Each question has a time limit (default: 30 seconds).
- **Quit Option**: The player can quit at any time by pressing the 'q' key.
- **Dynamic Display**: The screen is split into two sections:
  - The top section shows the current level and score.
  - The bottom section displays the current question and the remaining time.

## Prerequisites
- Python 3.x
- `curses` library (usually comes with Python standard library on Unix-based systems like Linux and macOS).

## Installation
1. Clone or download this repository to your local machine.

   ```
   git clone https://github.com/yourusername/python-quiz-game.git
2. Navigate to the project folder.

    ```
    cd python-quiz-game
## Running the Game
1. Open a terminal in the project folder.
2. Run the game using Python:

    ```
    python quiz_game.py
- Use the arrow keys to navigate.
- Answer questions by typing your response and pressing Enter.
- Press 'q' at any time to quit the game.

## Game Overview

1. The game will ask you a series of arithmetic questions, which will be displayed on the bottom part of the screen.
2. Each question has a time limit of 30 seconds (you can adjust the time limit in the code if needed).
3. Your score will be displayed in the top part of the screen, and your progress through the levels will be shown as well.
4. After completing each level, you'll be prompted to continue to the next level, or quit by pressing the 'q' key.

## Example
### Level 1: Two-Digit Addition

    ```
    +----------------------------------------+
    | Level: 1                               |
    | Score: 3                               |
    +----------------------------------------+
    +----------------------------------------+
    | Question 4/10:                         |
    | What is 45 + 67?                       |
    | Time remaining: 28 seconds             |
    | Your answer: 112                       |
    | Correct!                               |
    +----------------------------------------+

### Level 2: Three-Digit Addition

    ```
    +----------------------------------------+
    | Level: 2                               |
    | Score: 5                               |
    +----------------------------------------+
    +----------------------------------------+
    | Question 5/10:                         |
    | What is 325 + 578?                     |
    | Time remaining: 20 seconds             |
    | Your answer: 903                       |
    | Correct!                               |
    +----------------------------------------+

## Keybindings:

- Enter: Submit your answer.
- Backspace: Remove the last digit from your answer.
- q: Quit the game at any time.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This game uses Python's curses library to handle terminal-based UI and input handling.
The game is intended to help improve basic arithmetic skills while providing an interactive and timed quiz experience.
