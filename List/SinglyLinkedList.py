class SList:
    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, p):
        p.next = SList.Node(item, p.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError('underflow')
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):
        if self.is_empty():
            raise IndexError("underflow")
        else:
            t = p.next
            p.next = t.next
            self.size -= 1

    def search(self, target_item):
        p = self.head
        for k in range(self.size):
            if target_item == p.item: return k
            p = p.next
        return None


