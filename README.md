# Number Guessing Game

This project is a simple Number Guessing Game built in Python using Test-Driven Development (TDD). 
The program generates a random number between 1 and 100, and the player tries to guess it. 
The game provides feedback after each guess and tracks the number of attempts.

## Contributors
- Akshaya Baitinti
- Sishir Gottumukkala

## Description
The game was developed collaboratively using pair programming. 
We followed the TDD approach to ensure that each part of the logic was tested and working before adding new features.

The player is repeatedly prompted to guess a number until they get it right. 
If the guess is too high or too low, the program gives feedback. 
When the correct number is guessed, the program displays the total number of attempts.

## Features
- Generates a random number between 1 and 100
- Provides feedback for each guess (Too low, Too high, Correct)
- Validates user input
- Tracks number of attempts
- Includes automated unit tests

## Development Process (TDD)
1. Wrote unit tests for the main logic in `test_guess.py`
2. Implemented functions in `main.py` to pass each test
3. Refactored and cleaned the code after tests passed

## How to Run the Game
Open the terminal in VS Code and run:
```bash
python3 main.py
