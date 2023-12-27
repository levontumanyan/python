import binary_tree
import unittest

class TestBinaryTree(unittest.TestCase):
	def test_empty_binary_tree(self):
		"""Test that the root of an empty binary tree is None"""
		tree = binary_tree.BinaryTree()
		self.assertEqual(tree.root, None)

	def test_one_append_to_empty_binary_tree(self):
		"""Test that we can append to an empty binary tree"""
		tree = binary_tree.BinaryTree()
		tree.append(5)
		self.assertEqual(tree.root.value, 5)
		self.assertFalse(tree.root.left_child)
		self.assertFalse(tree.root.right_child)

	def test_multiple_appends_to_binary_tree(self):
		"""Test that we can append to a binary tree"""
		tree = binary_tree.BinaryTree()
		tree.append(5)
		tree.append(3)
		tree.append(7)
		self.assertEqual(tree.root.value, 5)
		self.assertEqual(tree.root.left_child.value, 3)
		self.assertEqual(tree.root.right_child.value, 7)
		self.assertFalse(tree.root.left_child.left_child)
		self.assertFalse(tree.root.left_child.right_child)
		self.assertFalse(tree.root.right_child.left_child)
		self.assertFalse(tree.root.right_child.right_child)

if __name__ == '__main__':
    unittest.main()