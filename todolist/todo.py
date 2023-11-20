import re
import board

class Todo():
	def __init__(self, todo_date, todo_text):
		if not board.Board.getInstance(board.Board):
			board.Board()
		if board.Board.get_todos_dict():
			self.todo_date = todo_date
			self.todo_text = todo_text
			for key in board.Board.get_todos_dict():
				if (key == hash(self)):
					print("This todo task already exists.")
					return False
				else:
					print("Todo added to your board")
	
			board.add_todo(self)	
		else:
			print("Todo added to your board")
			self.todo_date = todo_date
			self.todo_text = todo_text
			board.Board.add_todo(self)

	def __hash__(self):
		return hash((self.todo_date, self.todo_text))
