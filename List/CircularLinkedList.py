class Clist:
    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self.last = self.Node(None, None)
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        n = self.Node(item, None)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1

    def first(self):
        if self.is_empty():
            raise IndexError
        f = self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            raise IndexError
        x = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print("empty")
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, '->', end="")
            print(p.item)
