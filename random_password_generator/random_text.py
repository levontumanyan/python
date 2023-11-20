import random
import string

def get_random_string(length):
	# choose from all lowercase letter
	letters = string.ascii_lowercase
	result_str = ''.join(random.choice(letters) for i in range(length))
	print(f"Random string of length, {length}, is: {result_str}")
	return result_str 
	#list1 = (random.choice(letters) for i in range(length))

def get_length_from_user():
	try:
		password_length = int(input("Please enter the desired length of the random password:  "))
	except (TypeError, ValueError):
    # Handle the exception
		print('Please enter an integer')
		return None
	return password_length

def get_complexity_from_user():
	try:
		password_complexity = str(input('Please enter the desired complexity of the random password: e.g. "weak", "medium", "strong" ) '))
	except (TypeError, ValueError):
    # Handle the exception
		print('Please enter a string for desired password length and complexity level (e.g. "weak", "medium", "strong").')
		return None
	return password_complexity

def is_user_length_valid(input):
	if int(input) < 12 or int(input) > 30:
		print("Please enter a length between 12-30")
		return False
	else:
		return True

def is_user_complexity_valid(complexity):
	if complexity == "weak|medium|strong":
		return True
	else:
		return False


while True:
	#get_random_string(get_length_from_user())
	password_length = get_length_from_user()
	password_complexity = get_complexity_from_user()

	if password_length or password_complexity is None:
		continue

	if not is_user_length_valid(password_length) or not is_user_complexity_valid(password_complexity):
		continue
	else:
		get_random_string(password_length)
	

#get_random_string(8)
#get_random_string(6)
#get_random_string(4)

