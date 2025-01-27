import curses
import random
import time


class Question:
    def __init__(self, question, answer, timeout=30):
        self.question = question
        self.answer = answer
        self.timeout = timeout

    def ask(self, bottom_window, current_question, total_questions):
        # Clear the bottom window for the current question
        bottom_window.clear()
        bottom_window.box()  # Add a border for better UI
        bottom_window.addstr(1, 2, f"Question {current_question}/{total_questions}:", curses.color_pair(2))
        bottom_window.addstr(3, 4, self.question, curses.color_pair(2))
        bottom_window.refresh()

        start_time = time.time()
        elapsed = 0
        user_input = ""

        while elapsed < self.timeout:
            # Display timer and user input dynamically
            bottom_window.addstr(5, 2, f"Time remaining: {self.timeout - int(elapsed)} seconds", curses.color_pair(2))
            bottom_window.addstr(6, 2, f"Your answer: {user_input}", curses.color_pair(2))
            bottom_window.refresh()

            try:
                # Non-blocking user input
                bottom_window.nodelay(True)
                key = bottom_window.getch()
                if key == -1:  # No key pressed
                    pass
                elif key == 10:  # Enter key
                    break
                elif 48 <= key <= 57:  # Numeric input (0-9)
                    user_input += chr(key)
                elif key == 127:  # Backspace
                    user_input = user_input[:-1]
                elif key == ord('q'):  # Quit on 'q'
                    return 'quit'
            except Exception:
                pass

            elapsed = time.time() - start_time

        bottom_window.nodelay(False)  # Reset input mode
        if elapsed >= self.timeout:
            bottom_window.addstr(8, 2, "Time's up!", curses.color_pair(1))
            bottom_window.refresh()
            time.sleep(1)
            return False
        try:
            return int(user_input) == self.answer
        except ValueError:
            return False


class Level:
    def __init__(self, number, num_questions=10, timeout=30):
        self.number = number
        self.num_questions = num_questions
        self.timeout = timeout
        self.questions = self.generate_questions()
        self.score = 0

    def generate_questions(self):
        questions = []
        for _ in range(self.num_questions):
            if self.number == 1:  # Two-digit addition
                a, b = random.randint(10, 99), random.randint(10, 99)
                question_text = f"What is {a} + {b}?"
                answer = a + b
            elif self.number == 2:  # Three-digit addition
                a, b = random.randint(100, 999), random.randint(100, 999)
                question_text = f"What is {a} + {b}?"
                answer = a + b
            elif self.number == 3:  # Two-digit subtraction
                a, b = random.randint(10, 99), random.randint(10, 99)
                if b > a:
                    a, b = b, a  # Ensure no negative results
                question_text = f"What is {a} - {b}?"
                answer = a - b
            elif self.number == 4:  # Three-digit subtraction
                a, b = random.randint(100, 999), random.randint(100, 999)
                if b > a:
                    a, b = b, a  # Ensure no negative results
                question_text = f"What is {a} - {b}?"
                answer = a - b
            elif self.number == 5:  # One-digit multiplication
                a, b = random.randint(1, 9), random.randint(1, 9)
                question_text = f"What is {a} * {b}?"
                answer = a * b
            elif self.number == 6:  # Two-digit multiplication
                a, b = random.randint(10, 99), random.randint(10, 99)
                question_text = f"What is {a} * {b}?"
                answer = a * b
            elif self.number == 7:  # Three-digit multiplication
                a, b = random.randint(100, 999), random.randint(100, 999)
                question_text = f"What is {a} * {b}?"
                answer = a * b
            elif self.number == 8:  # Two-digit division
                # Ensure the divisor is not zero and the division result is a whole number
                a = random.randint(10, 99) * random.randint(1, 9)  # Make sure division is exact
                b = random.randint(1, 9)  # Non-zero divisor
                question_text = f"What is {a} ÷ {b}?"
                answer = a // b  # Integer division
            else:
                raise ValueError("Unsupported level number.")
            questions.append(Question(question_text, answer, self.timeout))
        return questions

    def play(self, top_window, bottom_window):
        top_window.clear()
        top_window.box()
        top_window.addstr(1, 2, f"Level: {self.number}", curses.color_pair(1))
        top_window.addstr(2, 2, f"Score: {self.score}", curses.color_pair(1))
        top_window.refresh()

        for i, question in enumerate(self.questions, 1):
            # Update the top window with level and score
            top_window.clear()
            top_window.box()
            top_window.addstr(1, 2, f"Level: {self.number}", curses.color_pair(1))
            top_window.addstr(2, 2, f"Score: {self.score}", curses.color_pair(1))
            top_window.refresh()

            # Ask the question in the bottom window
            result = question.ask(bottom_window, i, self.num_questions)
            if result == 'quit':
                return 'quit'
            elif result:
                self.score += 1
                bottom_window.addstr(8, 2, "Correct!", curses.color_pair(2))
            else:
                bottom_window.addstr(8, 2, f"Wrong! The correct answer was {question.answer}.", curses.color_pair(2))
            bottom_window.refresh()
            time.sleep(1)

        return self.score


def main(stdscr):
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLUE)  # Top window color
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Bottom window color

    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    # Get the screen size
    height, width = stdscr.getmaxyx()

    # Create two windows: top (level and score) and bottom (current question)
    top_window = stdscr.subwin(height // 3, width, 0, 0)  # Top third of the screen
    bottom_window = stdscr.subwin((2 * height) // 3, width, height // 3, 0)  # Bottom two-thirds

    # Create and play levels
    num_levels = 8
    for level_num in range(1, num_levels + 1):
        level = Level(level_num)
        result = level.play(top_window, bottom_window)
        if result == 'quit':
            break

        # After level completion
        bottom_window.clear()
        bottom_window.box()
        bottom_window.addstr(1, 2, f"Level {level_num} complete! Your score: {level.score}/{level.num_questions}", curses.color_pair(2))
        bottom_window.addstr(3, 2, "Press any key to continue to the next level.", curses.color_pair(2))
        bottom_window.refresh()
        bottom_window.getch()

    # End of game
    stdscr.clear()
    stdscr.addstr(1, 2, "Game Over! Thanks for playing.", curses.color_pair(1))
    stdscr.refresh()
    time.sleep(2)


if __name__ == "__main__":
    curses.wrapper(main)
