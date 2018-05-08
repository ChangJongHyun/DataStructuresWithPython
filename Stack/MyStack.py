import copy


class Stack:
    class Node:
        def __init__(self, item, link=None):
            self.item = item
            self.next = link

    def __init__(self):
        self.size = 0
        self.top = None

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.top = self.Node(item, self.top)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyError("underflow")
        else:
            n = self.top
            self.top = self.top.next
            self.size -= 1
            return n.item

    def peek(self):
        if self.size != 0:
            return self.top.item

    def __str__(self):
        tmp = copy.deepcopy(self)
        string = ""
        for i in range(tmp.size):
            item = tmp.top.item
            if tmp.top.next is None:
                string += str(item)
                tmp.pop()
            else:
                string += str(item) + "->"
                tmp.pop()
        return string


class EmptyError(Exception):
    pass
