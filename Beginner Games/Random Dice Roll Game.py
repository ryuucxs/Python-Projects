import random


while True:

    choose = input("Do you want to roll the dice? (yes/no): ")
    if choose.lower() == "yes":
        num_dice = int(input("How many dice do you want to roll? "))
        for i in range(num_dice):
            dice_roll = random.randint(1, 6)
            print(f"You rolled: {i+1}: {dice_roll}")

    elif choose.lower() == "no":
        print("Thanks for playing!")
        break

    else:
        print("Invalid input, please type 'yes' or 'no'.")

