class BinaryHeap:
    def __init__(self, a):
        self.a = a  # 리스트
        self.N = len(a) - 1  # 항목 수

    def create_heap(self):
        for i in range(self.N / 2, 0, -1):
            self.downHeap(i)

    def insert(self, key_value):
        self.N += 1
        self.a.append(key_value)
        self.upheap(self.N)

    def delete_min(self):
        if self.N is 0:
            print("empty heap")
            return None
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.N -= 1
        self.downHeap(1)
        return minimum

    def downHeap(self, i):  # 힙을 내려가며 힙속성 회복
        while 2 * i <= self.N:
            k = 2 * i
            if k < self.N and self.a[k][0] > self.a[k + 1][0]:
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k

    def upHeap(self, j):  # 힙을 올라가며 힙속성 회복
        while j > 1 and self.a[j // 2][0] > self.a[j][0]:
            self.a[j], self.a[j // 2] = self.a[j // 2], self.a[j]
            j = j // 2

    def print_heap(self):
        for i in range(1, self.N + 1):
            print("[%2d" % self.a[i][0], self.a[i][0], "]", end="")
        print("\n힙 크기= ", self.N)
