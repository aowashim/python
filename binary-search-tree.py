# This code is for creating a binary search tree
# and it will print inorder traversal
class Node:

    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

    def insertNode(self, data):
        if self.key > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insertNode(data)

        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insertNode(data)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end = ' ')
        if self.right:
            self.right.inorder()

root = Node(8)
print(root)
root.insertNode(3)
root.insertNode(6)
root.insertNode(12)
root.insertNode(34)
root.inorder()
print('\n')