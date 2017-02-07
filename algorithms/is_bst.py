class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(4)
root.left = Node(11)
root.right = Node(5)


def inorder(root):
    if root:
        inorder(root.left)
        print root.data
        inorder(root.right)

inorder(root)


def is_bst(node, min_key, max_key):
    if not node:
        return True
    if node.data < min_key or node.data > max_key:
        return False
    is_bst(node.left, min_key, node.data)
    is_bst(node.right, node.data, max_key)


print is_bst(root, -float('inf'), float('inf'))