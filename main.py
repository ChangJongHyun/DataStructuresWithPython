from HashTable.MyLinearProb import LinearProbing
from List.DoublyLinkedList import DList
import Stack.MyStack as stack
import Queue.MyQueue as q
import Queue.MyDequeue as dq
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
    t = LinearProbing(13)
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon')
    print("탐색 결과:")
    print('50의 데이터 = ', t.get(50))
    print('63의 데이터 = ', t.get(63))
    print('Hash Table')
    t.print_table()
