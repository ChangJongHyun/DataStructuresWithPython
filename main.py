from List.DoublyLinkedList import DList
import Stack.MyStack as stack
import Queue.MyQueue as q
import copy


def is_palindrome(str):
    s = stack.Stack()
    half = int(len(str) / 2)
    for i in range(half):
        s.push(str[i])

    if len(str) % 2 == 1:
        half += 1

    while s.size != 0:
        if s.pop() == str[half]:
            half += 1
        else:
            return False
    return True


def parentheses(str):
    s = stack.Stack()
    item = {'{': '}', '(': ')'}
    for i in range(len(str) - 1):
        if str[i] == '{' or str[i] == '(':
            s.push(str[i])
        if s.peek() is None:
            return False
        if item[s.peek()] == str[i + 1]:
            s.pop()
    return s.size == 0


def reverse_stack(item):
    tmp = copy.deepcopy(item)
    reverse = stack.Stack()
    for i in range(tmp.size):
        reverse.push(tmp.pop())
    return reverse


if __name__ == '__main__':
    s = stack.Stack()
    q = q.Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    print(q)
    q.remove()
    q.remove()
    q.remove()
    q.add(3)
    q.add(2)
    q.add(1)
    s.push(1)
    s.push(2)
    s.push(3)
    print(q)
    r = reverse_stack(s)
    print("origin: " + str(s))
    print("reverse: " + str(r))
    print(parentheses("{{(){()}}}"))
    print(is_palindrome("rer"))
