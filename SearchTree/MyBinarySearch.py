class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, root, k):
        if root is None:
            return None
        if root.key > k:
            return self.get_item(root.left, k)
        elif root.key < k:
            return self.get_item(root.right, k)
        else:
            return root.value

    def put(self, key, value):
        self.root = self.put_item(self.root, Node(key, value))

    def put_item(self, node, item):
        if node is None:
            return item
        if node.value < item.value:
            self.put_item(node.right, item)
        elif node.value > item.value:
            self.put_item(node.left, item)
        return node

    def min(self):
        return self.min_item(self.root)

    def min_item(self, node):
        if node is None:
            raise EmptyTree("empty tree")
        if node.left is None:
            return node
        return self.min_item(node.left)

    def delete_min(self):
        if self.root is None:
            raise EmptyTree("empty tree")
        self.root = self.del_min(self.root)  # 루트 노트를 새로 업데이트

    def del_min(self, node):
        if node.left is None:  # 최소인 노드를 찾고, 그 노드의 right 값 리턴(값 교환)
            return node.right
        node.left = self.del_min(node.left)  # 리턴받은 right 값을 부모 노드의 left 값으로 저장
        return node  # 업데이트 된 노드를 반환

    def delete(self, key):
        self.root = self.del_item(self.root, key)

    def del_item(self, node, key):
        if node is None:
            return None
        if node.key > key:
            node.left = self.del_item(node.left, key)
        elif node.key < key:
            node.right = self.del_item(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            target = node
            node = self.min_item(target.right)
            node.right = self.del_min(target.right)
            node.left = target.left
        return node


class EmptyTree(Exception):
    pass
