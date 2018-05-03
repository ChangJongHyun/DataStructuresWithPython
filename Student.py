class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


best = Student("lee", 100)
print(best.get_id())
print(best.get_name())

a = range(20)
print(range(10))
print(range(1, 11))
print(range(10, 20, 2))
print(range(10, 1, -1))
print(range(len(a)))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))