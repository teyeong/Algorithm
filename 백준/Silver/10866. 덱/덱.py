from sys import stdin

def input():
    return stdin.readline().rstrip()

deque = []

def push_front(value):
    deque.insert(0, value)
    return

def push_back(value):
    deque.append(value)
    return

def pop_front():
    if len(deque) > 0:
        return deque.pop(0)
    return -1

def pop_back():
    if len(deque) > 0:
        return deque.pop()
    return -1

def size():
    return len(deque)

def empty():
    if len(deque) == 0:
        return 1
    return 0

def front():
    if len(deque) > 0:
        return deque[0]
    return -1

def back():
    if len(deque) > 0:
        return deque[-1]
    return -1

N = int(input())
    
for i in range(N):
    comm = input()
    
    if "push_front" in comm:
        value = int(comm.split()[1])
        push_front(value)
    elif "push_back" in comm:
        value = int(comm.split()[1])
        push_back(value)
    elif comm == "pop_front":
        print(pop_front())
    elif comm == "pop_back":
        print(pop_back())
    elif comm == "size":
        print(size())
    elif comm == "empty":
        print(empty())
    elif comm == "front":
        print(front())
    elif comm == "back":
        print(back())