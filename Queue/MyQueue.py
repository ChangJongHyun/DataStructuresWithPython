import copy


class Queue:
    class Node:
        def __init__(self, item, n):
            self.item = item
            self.next = n

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
            self.tail = self.head
        else:
            self.tail.next = self.Node(item, None)
            self.tail = self.tail.next
        self.size += 1

    def remove(self):
        if self.is_empty():
            raise EmptyError("underflow")
        else:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
        self.size -= 1

    def pop(self):
        if self.is_empty():
            raise EmptyError("underflow")
        else:
            n = self.head.item
            self.remove()
            return n

    def __str__(self):
        string = ""
        tmp = copy.deepcopy(self)
        for i in range(tmp.size):
            item = tmp.pop()
            if tmp.size is 0:
                string += str(item)
            else:
                string += str(item) + "<--"
        return string


class EmptyError(Exception):
    pass
