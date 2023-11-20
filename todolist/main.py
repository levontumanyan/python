from board import Board
from todo import Todo
import re
from datetime import datetime

# board = Board()
# todo1 = Todo(2022, "Hello World what's hapenning")
# todo2 = Todo(2021, "Hello World what's hapenning")
# todo3 = Todo(2020, "Hello World what's hapenning")
# todo4 = Todo(2019, "Hello World what's hapenning")
# todo5 = Todo(2018, "Hello World what's hapenning")
# todo6 = Todo(2017, "Hello World what's hapenning")

def get_todo_message_from_user():
	todo_text = input("Please enter the message of the todo: ")
	todo_text = sanitize_input(todo_text, 300)

	if validate_input(todo_text):
		return todo_text

def get_todo_date_from_user():
	todo_date_year = input("Please enter the year (yyyy) : ")
	todo_date_month = input("Please enter the month (mm) : ")
	todo_date_day = input("Please enter the day (dd): ")
	
	todo_date_year = sanitize_input(todo_date_year, 5)
	todo_date_month = sanitize_input(todo_date_month, 3)
	todo_date_day = sanitize_input(todo_date_day, 3)

	if ( int(todo_date_year) > 2300 or int(todo_date_year) < 2020 or int(todo_date_month) > 12 or int(todo_date_month) < 1 or int(todo_date_day) > 31 or int(todo_date_day) < 1 ):
		print("Please enter valid dates")
		return None

	if validate_input(todo_date_year) and validate_input(todo_date_month) and validate_input(todo_date_day):
		todo_date = f"{todo_date_year}-{todo_date_month}-{todo_date_day}"
		try:
			date = datetime.strptime(todo_date, "%Y-%m-%d")
			print("Date:", date)
			return date
		except ValueError:
			print("Use numbers only for the dates: yyyy: 2020, mm: 08, dd:26")
			#raise Exception("The date is not in the correct format")
			return None

def validate_input(user_input):
    # Use regular expressions to check for any unwanted characters
	pattern = re.compile('^[a-zA-Z0-9 ]+$')
	if pattern.match(user_input):
		print("Input Validated")
		return True
	else:
		return False

def sanitize_input(user_input, max_length):
    # Remove any leading or trailing whitespace
    user_input = user_input.strip()
    # Limit the length of the input to 200 characters
    user_input = user_input[:max_length-1]
    return user_input

def main():
	while True:

		# if ( year > 2300 or month > 12 or month < 1 or day > 31 or day < 1 ):
		# 	print("Please enter valid dates")
		# 	continue
		
		#print("Would you like to add a new todo or list your todo board?: ")
		#print("- add")
		#print("- list")



		#todo_date = get_todo_date_from_user()
		# try:
		# 	todo_date = get_todo_date_from_user()
		# except Exception:
		# 	print("BIG ERROR: FORMAT main loop")
		# 	continue
		todo_date = get_todo_date_from_user()

		if not todo_date:
			continue

		todo_text = get_todo_message_from_user()

		if todo_text:
			todo_new = Todo(todo_date, todo_text)
			#Board.add_todo(todo_new)
		else:
			print("Please enter the date and the message for your todo.")
			continue
		Board.print_board()

if __name__ == '__main__':
	main()
