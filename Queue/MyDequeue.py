import copy


class DeQueue:
    class Node:
        def __init__(self, item, prev, next):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.size is 0

    def size(self):
        return self.size

    def add_front(self, item):
        if self.is_empty():
            self.front = self.Node(item, None, None)
            self.rear = self.front
        else:
            self.front.next = self.Node(item, self.front, "front")
            self.front = self.front.next
        self.size += 1

    def add_rear(self, item):
        if self.is_empty():
            self.rear = self.Node(item, None, None)
            self.front = self.rear
        else:
            self.rear.prev = self.Node(item, "rear", self.rear)
            self.rear = self.rear.prev
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            raise EmptyError("Underflow")
        else:
            if self.front is self.rear:
                self.rear = None
                self.front = None
            else:
                self.front = self.front.prev
            self.size -= 1

    def remove_rear(self):
        if self.is_empty():
            raise EmptyError("Underflow")
        else:
            if self.rear is self.front:
                self.rear = None
                self.front = None
            else:
                self.rear = self.rear.next
            self.size -= 1

    def pop_front(self):
        n = self.front.item
        self.remove_front()
        return n

    def pop_rear(self):
        n = self.rear.item
        self.remove_rear()
        return n

    def __str__(self):
        string = "front: "
        tmp = copy.deepcopy(self)
        for i in range(tmp.size):
            if tmp.size is 1:
                string += str(tmp.pop_front())
            else:
                string += str(tmp.pop_front()) + " -- "
        return string + " :rear"


class EmptyError(Exception):
    pass
