try:
	with open('random.txt') as file:
		my_list = [ line for line in file ]
except(FileNotFoundError):
	print("File not found")

print(my_list)

