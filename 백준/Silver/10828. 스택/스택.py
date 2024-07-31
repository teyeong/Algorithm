import sys

N = int(input())

stack = []

for _ in range(N):
    comm = sys.stdin.readline().rstrip()
    if comm == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif comm == "size":
        print(len(stack))
    elif comm == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif comm == "empty":
        if stack:
            print(0)
        else:
            print(1)
    else:
        _, num = comm.split()
        stack.append(int(num))