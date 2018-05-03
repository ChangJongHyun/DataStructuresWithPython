class DList:
    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)
        t.next = n
        p.prev = n
        self.size += 1

    def insert_after(self, p, item):
        t = p.next
        n = self.Node(item, p, t)
        t.prev = n
        p.next = n
        self.size += 1

    def delete(self, x):
        prev = x.prev
        next = x.next
        prev.next = next
        next.prev = prev
        self.size -= 1

    def print_list(self):
        if self.is_empty():
            print("empty list")
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end="")
                else:
                    print(p.item)
                p = p.next
