numbers = [2, 34, 323, 230, 20, 49, 384, 305, 285, 23, 48, 9]

even_numbers = 0
odd_numbers = 0

for i in numbers:
	if i % 2 == 0:
		even_numbers += 1
	else:
		odd_numbers += 1

print(f"In the List or this many odd numbers: {odd_numbers}")
print(f"In the List or this many even numbers: {even_numbers}")