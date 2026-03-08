import random

while True:
        play = input("Do you want to play a number guessing game? (y/n): ")
        if play.lower() == "y":
                number_to_guess = random.randint(1, 50)
                attempts = 5
                print("I have selected a number between 1 and 50. You have 5 attempts to guess it.")
                while attempts > 0:
                        try:
                                guess = int(input("Enter your guess: "))
                                if guess < 1 or guess > 50:
                                        print("Please guess a number within the range of 1 to 50.")
                                        continue
                                if guess == number_to_guess:
                                        print("Congratulations! You've guessed the correct number!")
                                        break
                                elif guess < number_to_guess:
                                        print("Too low!")
                                else:
                                        print("Too high!")
                                attempts -= 1
                                print(f"You have {attempts} attempts left.")
                        except ValueError:
                                print("Invalid input. Please enter a numeric value.")
                else:
                        print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")
        elif play.lower() == "n":
                print("Thanks for playing! Goodbye.")
                break
        else:
                print("Invalid input. Please enter 'y' or 'n'.")
