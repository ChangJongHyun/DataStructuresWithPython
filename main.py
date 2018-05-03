from List.DoublyLinkedList import DList
import Stack.MyStack as stack


def is_palindrome(str):
    s = stack.Stack()
    half = int(str.__len__() / 2)
    for i in range(half):
        s.push(str[i])

    if is_odd(str):
        half += 1

    while s.size != 0:
        a = s.pop()
        b = str[half]
        if a == b:
            half += 1
        else:
            return False
    return True


def is_odd(str):
    return str.__len__() % 2 == 1


if __name__ == '__main__':
    s = stack.Stack()

    s.push('{')
    s.push('(')
    s.push('[')

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(is_palindrome('RACECAR'))