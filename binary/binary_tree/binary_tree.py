
class Node():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None



# class Tree

class BinaryTree():
    def __init__(self):
        self.root = None

    def append(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._append( value, self.root )

    def _append(self, value, current_node):
        # if we are here then the head is already a certain node

        #while current_node.left_child or current_node.right_child:
        #    if ( new_node.value > current_node.value ):
        if value < current_node.value:
            if not current_node.left_child:
                current_node.left_child = Node(value)
            else:
                current_node = current_node.left_child
                self._append( value, current_node )
        else:
            if not current_node.right_child:
                current_node.right_child = Node(value)
            else:
                current_node = current_node.left_child
                self._append( value, current_node )

    def in_order_traversal(self):
        if self.root:
            self._in_order_traversal(self.root)
        else:
            return None
    
    def _in_order_traversal(self, current_node):
        if current_node.left_child:
            self._in_order_traversal(current_node.left_child)
        print(current_node.value)
        #yield current_node.value
        if current_node.right_child:
            self._in_order_traversal(current_node.right_child)

# create a function that will print the tree in order traversal iterator generator
    def in_order_traversal_iter(self):
        if self.root is None:
            return
        yield from self._in_order_traversal_iter(self.root)

    def _in_order_traversal_iter(self, current_node):
        if current_node.left_child is not None:
            yield from self._in_order_traversal(current_node.left_child)
        yield current_node.value
        if current_node.right_child is not None:
            yield from self._in_order_traversal(current_node.right_child)
    
    def __len__(self):
        if self.root:
            return self._len(self.root)
        else:
            return 0
    
    def _len(self, current_node):
        if current_node.left_child:
            self._len(current_node.left_child)
        if current_node.right_child:
            self._len(current_node.right_child)
        return 1


def main():
    tree = BinaryTree()
    tree.append(5)
    tree.append(3)
    tree.append(7)
    tree.in_order_traversal()
    tree_iter = tree.in_order_traversal_iter()
    print(next(tree_iter))
    print(len(tree))


    
if __name__ == "__main__":
    #load_template()
    #create_invoice()
    main()