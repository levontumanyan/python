

# User will hav e 

while True:
	print('''
		Weak: Only contains lowercase letters and numbers
		Medium: Contains lowercase and uppercase letters, numbers, and special characters
		Strong: Contains lowercase and uppercase letters, numbers, special characters and minimum length of 12 characters ''')
	user_req = input('Please enter the desired password length (12-32) and complexity level (e.g. "weak", "medium", "strong"): ')
	length, complexity = user_req.split()
	
