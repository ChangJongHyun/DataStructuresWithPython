from List.SinglyLinkedList import SList


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
        if self.is_empty():
            self.top = self.Noe(item, self.)

        self.top = self.Node(item, self.top)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyError("underflow")
        else:
            n = self.top
            self.top = self.top.next
            return n.item

    def peek(self):
        if self.size != 0:
            return self.top.item


class EmptyError(Exception):
    pass
