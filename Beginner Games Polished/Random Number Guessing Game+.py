import random
from typing import Dict, Optional

# Difficulty settings
difficulty_settings: Dict[str, Dict] = {
    'easy': {'attempts': 10, 'range': 50, 'points': 5},
    'medium': {'attempts': 7, 'range': 100, 'points': 10},
    'hard': {'attempts': 5, 'range': 200, 'points': 20},
    'random': {'attempts': random.randint(3, 15), 'range': random.randint(50, 500), 'points': random.randint(1, 50)}
}

def ask_for_difficulty() -> Optional[str]:
    """Ask the user if they want to play and choose a difficulty."""
    while True:
        try:
            play = input("\nDo you want to play a game of Number Guessing? (yes/no): ").lower().strip()
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            return None

        if play == 'yes':
            print("\nWelcome to the Number Guessing Game! Difficulty settings:")
            print("Easy (10 attempts, numbers 1-50, 5 points per correct guess)")
            print("Medium (7 attempts, numbers 1-100, 10 points per correct guess)")
            print("Hard (5 attempts, numbers 1-200, 20 points per correct guess)")
            print("Random (random attempts, numbers 1-500, random points per correct guess)")
            
            while True:
                difficulty = input("\nChoose a difficulty (Easy, Medium, Hard, Random): ").strip().lower()
                if difficulty in difficulty_settings:
                    return difficulty
                else:
                    print("Invalid difficulty. Please choose 'Easy', 'Medium', 'Hard', or 'Random'.")
        elif play == 'no':
            print("Thank you for playing! Goodbye!")
            return None
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def choose_difficulty(difficulty_user: str) -> Optional[Dict]:
    """Return the settings for the chosen difficulty."""
    return difficulty_settings.get(difficulty_user)

def play_game(attempts: int, number_range: int, points_per_correct: int, score: int) -> int:
    """Main game loop for guessing numbers."""
    secret_number = random.randint(1, number_range)
    print(f"\nYou have {attempts} attempts to guess a number between 1 and {number_range}.")

    while attempts > 0:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            break

        if guess < 1 or guess > number_range:
            print(f"Please guess a number within 1 to {number_range}.")
            continue

        if guess == secret_number:
            score += points_per_correct
            print(f"Congratulations! You guessed the correct number {secret_number}!")
            print(f"You earned {points_per_correct} points. Total score: {score}")
            break
        elif abs(guess - secret_number) <= 10:
            attempts -= 1
            if guess < secret_number:
                print("You're very close! Try a slightly higher number.")
            else:
                print("You're very close! Try a slightly lower number.")
        else:
            attempts -= 1
            if guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

        if attempts == 0:
            print(f"\nYou've run out of attempts. The correct number was {secret_number}.")

    return score

def main() -> None:
    score = 0
    while True:
        difficulty_user = ask_for_difficulty()
        if difficulty_user is None:
            break

        settings = choose_difficulty(difficulty_user)
        if not settings:
            continue

        attempts = settings['attempts']
        number_range = settings['range']
        points_per_correct = settings['points']

        score = play_game(attempts, number_range, points_per_correct, score)

        while True:
            try:
                play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            except KeyboardInterrupt:
                print("\nGame interrupted. Goodbye!")
                return

            if play_again == 'no':
                print(f"Thank you for playing!")
                print(f"Your final score is: {score} points.")
                return
            elif play_again == 'yes':
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()