items_and_price = {}
print("Hello dear customer!")

bill = 0
try:
	while True:
		ask_what_to_do = input("\n Do you want to:\n" 
							 "1. Add something to your shopping list \n"
							 "2. Edit something on your shopping list \n"
							 "3. Delete something on your shopping list \n"
							 "4. Show your shopping list \n"
							 "5. Get your bill and pay\n")
		if ask_what_to_do == "1":
			new_item = input("What is the name of the item you want to add? ")
			if new_item in items_and_price:
				print(f"The item {new_item} is already in your shopping list.")
				continue
			elif len(new_item) == 0:
				print("The item name cannot be empty.")
				continue
			new_item_price = float(input(f"How much does {new_item} cost? "))
			if new_item_price < 0:
				print("The price cannot be negative.")
				continue
			items_and_price[new_item] = new_item_price
			print(f"You successfully added {new_item} which costs {new_item_price}€.")

		elif ask_what_to_do == "2":
			what_to_edit = input("\nDo you want to edit an item or a price? \n"
						"1. item \n"
						"2. price \n")
			if what_to_edit == "1":
				which_item_edit = input("What is the name of the item you want to edit? ")
				if which_item_edit not in items_and_price:
					print(f"The item {which_item_edit} is not in your shopping list.")
					continue
				elif which_item_edit in items_and_price:
					new_item_name = input("What do you want the new item name to be? ")
					if len(new_item_name) == 0:
						print("The item name cannot be empty.")
						continue
					items_and_price[new_item_name] = items_and_price[which_item_edit]
					del items_and_price[which_item_edit]  # Or use items_and_prices.pop(which_item_edit)
					print(f"The item {which_item_edit} has been updated to {new_item_name}")
			elif what_to_edit == "2":
				which_item_edit = input("The price of which item from your shopping list do you want to edit?")
				if which_item_edit not in items_and_price:
					print(f"The item {which_item_edit} is not in your shopping list.")
					continue
				new_item_price = float(input(f"What is the new price you want on {which_item_edit}? "))
				if new_item_price < 0:
					print("The price cannot be negative.")
					continue
				items_and_price[which_item_edit] = new_item_price
				print(f"The new price of {which_item_edit} is {new_item_price}€.")
			else:
				print("Please type either 1 or 2.")

		elif ask_what_to_do == "3":
			while True:
				which_item_edit = input("What is the name of the item you want to delete? ")
				if which_item_edit not in items_and_price:
					print(f"The item {which_item_edit} does not exist in your shopping list")
					continue
				# Inner loop for confirmation
				while True:
					ask_again = input(f"Are you sure you want to delete {which_item_edit} ({items_and_price[which_item_edit]})? \
1. yes \
2. no ").lower()
					if ask_again == "yes":
						print(f"The item {which_item_edit} has been deleted!")
						del items_and_price[which_item_edit]
						break  # Exit confirmation loop
					elif ask_again == "no":
						print("Item not deleted.")
						break  # Exit confirmation loop
					else:
						print("Please type 'yes' or 'no'.")
						continue  # Ask again for confirmation
				break  # Exit item deletion loop

		elif ask_what_to_do == "4":
			if not items_and_price:
				print("Your shopping list is empty.")
			else:
				print("Your shopping list contains:")
				for item, price in items_and_price.items():
					print(f"{item}: {price}€")

		elif ask_what_to_do == "5":
			bill = sum(items_and_price.values())
			print(f"Your total price for todays shopping is {bill}€")
			break
		else:
			print("Type a number between 1 and 5 to choose an option")

except ValueError:
	print("Invalid input! Please enter a valid number or price.")