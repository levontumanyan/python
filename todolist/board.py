class Board():
	__instance_exists = False
	todos_dict = {}

	@staticmethod
	def getInstance(self):
		""" Static access method. """
		if Board.__instance_exists:
			return self
		else:
			return None	
		#return Board.__instance_exists
	
	def __init__(self):
		""" Virtually private constructor. """
		if Board.__instance_exists:
			return Board
		else:
			Board.__instance_exists = True

	def __str__(self):
		result = ""
		for key, value in Board.todos_dict.items():
			result += "Hash: " + str(key) + "      " + str(value) + "\n"
		return result
	
	def __len__(self):
		return len(Board.todos_dict)
	
	@staticmethod
	def print_board():
		for key, value in Board.todos_dict.items():
			print(f"todo_Date: {value[0]} , Message: {value[1]} ")		

	@staticmethod
	def add_todo(todo):
		Board.todos_dict[hash(todo)] = (todo.todo_date, todo.todo_text)

	@staticmethod
	def get_todos_dict():
		return Board.todos_dict
