import unittest
import main
import todo
import board
from datetime import datetime

class TestTodo(unittest.TestCase):
	
	#def setUp(self):
	#	self.todo_list = todo.Todo()
		
	def test_add_todo(self):
		todo_date = "2022-08-26"
		todo_message = "something blash"

		try:
			todso_date = datetime.strptime(todo_date, "%Y-%m-%d")
			print("Date:", todo_date)
			self.todo_list = todo.Todo(todo_date, todo_message)
		except ValueError:
			print("Use numbers only for the dates: yyyy: 2020, mm: 08, dd:26")
			#raise Exception("The date is not in the correct format")
			return None
		self.assertEqual( len(board.Board()), 1)

	def test_add_same_todo(self):
		todo_date1 = "2022-08-26"
		todo_message1 = "something blash"

		todo_date2 = "2022-08-26"
		todo_message2 = "something blash"

		try:
			todo_date1 = datetime.strptime(todo_date1, "%Y-%m-%d")
			todo_date2 = datetime.strptime(todo_date2, "%Y-%m-%d")
			
			self.todo_list = todo.Todo(todo_date1, todo_message1)
		except ValueError:
			print("Use numbers only for the dates: yyyy: 2020, mm: 08, dd:26")
			#raise Exception("The date is not in the correct format")
			return None
		self.assertEqual( len(board.Board()), 1)

class TestValidateInput(unittest.TestCase):
	text1 = "dsada213123"
	text2 = "//>sada1"
	text3 = "::"
	text4 = "asdsadasAA"
	text5 = "12312312312"
	text6 = "asdsadasAA"

	def test_validate_input(self):
		self.assertEqual( main.validate_input(TestValidateInput.text1), True)
		self.assertEqual( main.validate_input(TestValidateInput.text2), False)
		self.assertEqual( main.validate_input(TestValidateInput.text3), False)
		self.assertEqual( main.validate_input(TestValidateInput.text4), True)
		self.assertEqual( main.validate_input(TestValidateInput.text5), True)
		self.assertEqual( main.validate_input(TestValidateInput.text6), True)


if __name__ == '__main__':
    unittest.main()