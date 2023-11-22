# Specify the file path
file_path = '/Users/levontumanyan/Documents/python/nato_phonetic/alphabet.txt'

def parse_alphabet():
	with open(file_path, 'r') as file:
		alphabect_dict = {}
		# Read the file line by line
		for line in file:
			# Process each line as needed
			#print(line.strip())  # Print the line after removing leading and trailing whitespaces
			alphabet_tuple = line.split("=")
			#print(alphabet_tuple)
			letter=alphabet_tuple[0].strip("[]").strip("\"\"")
			word=alphabet_tuple[1].strip("[]").strip("\n").strip("\"\"")
			alphabect_dict[letter]=word
	return alphabect_dict

# Open the file in read mode
		
#print(parse_alphabet())

def phonetized(word):
	phonetized_list=[]
	word = word.upper()
	for ch in word:
		phonetized_list.append(parse_alphabet()[ch])
	return phonetized_list

try:
	
	while True:
		user_input = input("Enter the word that you want to be phonetized ( or quit to exit the program ): ")

		if (user_input.lower() == 'quit'):
			print("Exiting the game, goodbye!")
			break
		
		print(user_input + "=", end="")
		print(phonetized(user_input))
		pass

except KeyboardInterrupt:
	print("\nProgram interrupted by user. Exiting gracefully.")	
	# Additional cleanup or actions can be performed here if needed