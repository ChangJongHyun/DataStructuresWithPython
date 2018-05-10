class LinearProbing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size  # hash table
        self.d = [None] * size  # data

    def hash(self, key):
        return key % self.M

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] is None:
                self.a[i] = key
                self.d[i] = data
                return
            if self.a[i] is key:
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j) % self.M
            if i is initial_position:
                print("fail to add item")
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] is not None:
            if self.a[i] is key:
                return self.d[i]
            i = (initial_position + j) % self.M
            j += 1
            if i is initial_position:
                return None
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end="")
        print()
        for i in range(self.M):
            print("{:4}".format(str(self.a[i])), ' ', end="")
        print()
