import random

choices = ["Rock", "Paper", "Scissors"]
computer_wins = 0
human_wins = 0

print("Hey, I coded a Rock, Paper, Scissors game")

while True:
	try:
		ask_question = input("Do you want to play? (y/n): ")
		if ask_question.lower() == "y":
			choose_rps = input("Choose between Rock, Paper, Scissors: ")
			random_choice = random.randint(0, 2)
			computer_choice = choices[random_choice]
			if choose_rps == computer_choice:
				print(f"The computer chose {computer_choice}")
				print("That was a draw!")
			elif choose_rps == "Rock" and computer_choice == "Scissors":
				print(f"The computer chose {computer_choice}")
				print("Congrats, you won!")
				human_wins += 1
			elif choose_rps == "Scissors" and computer_choice == "Paper":
				print(f"The computer chose {computer_choice}")
				print("Congrats, you won!")
				human_wins += 1
			elif choose_rps == "Paper" and computer_choice == "Rock":
				print(f"The computer chose {computer_choice}")
				print("Congrats, you won!")
				human_wins += 1
			else:
				print(f"The computer chose {computer_choice}")
				print("Too bad, the computer won :(")
				computer_wins += 1
		elif ask_question.lower() == "n":
			print(f"The computer won {computer_wins} times.")
			print(f"You won {human_wins} times.")
			if computer_wins == human_wins:
				print("Damn, it's a draw again, we'll settle this some other time!")
			elif computer_wins > human_wins:
				print("You really suck at this!")
			else:
				print("Wow, you're really a master of Rock, Paper, Scissors")
			break
		else:
			print("Nigga write either y or n")
	except ValueError:
		print("Please write either Rock, Paper, or Scissors")
		continue
