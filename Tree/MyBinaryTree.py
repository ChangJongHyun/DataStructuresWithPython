class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


class MyBinaryTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def preorder(self, n):
        if n is not None:
            print(str(n.item), ' ', end="")
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        if n is not None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item), ' ', end="")
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        if n is not None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item), ' ', end="")

    def levelorder(self, root):
        q = []
        q.append(root)
        while len(q) is not 0:
            t = q.pop(0)
            print(str(t.item), ' ', end="")
            if t.left is not None:
                q.append(t.left)
            if t.right is not None:
                q.append(t.right)

    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
