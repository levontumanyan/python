# Implement a class node
# Implement a class binary tree, with a root node.

class Node():
	def __init__(self, value) -> None:
		self.value = value
		self.right_child = None
		self.left_child = None

class BinaryTree():
	def __init__(self) -> None:
		self.root = None

	def insert(self, node):
		current_node = self.root
		if not self.root:
			self.root = node
		else:
			self._insert(node, self.root)
	
	def _insert(self, node, current_node):
		if not current_node.left_child:
			current_node.left_child = node
		elif not current_node.right_child:
			current_node.right_child = node
		else:
			self._insert(node, current_node.left_child)

	def in_order_traversal(self):
		current_node = self.root
		stack = []
		while True:
			if current_node:
				stack.append(current_node)
				current_node = current_node.left_child
			elif stack:
				current_node = stack.pop()
				print(current_node.value)
				current_node = current_node.right_child
			else:
				break

	def remove(node):
		pass
	
	def get_root_node(self):
		return self.root



bt = BinaryTree()

nodes = [Node(i) for i in range(10)]

for node in nodes:
	bt.insert(node)

bt.in_order_traversal()