import random

def generate_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

def check_guess(guess, target):
    """Compare the guess with the target number and return a result string."""
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"

def play_game():
    """Main game loop for the number guessing game."""
    target = generate_number()
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess (1–100): "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1
            result = check_guess(guess, target)
            print(result)

            if result == "Correct!":
                print(f"You guessed it in {attempts} tries!")
                break

        except ValueError:
            print("Please enter a valid number.")

play_game()
